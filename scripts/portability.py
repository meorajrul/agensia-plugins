"""Filesystem and invocation budgets for this repository, not host certification."""
from pathlib import PurePosixPath, PureWindowsPath
import re
import unicodedata

# Repository policies are deliberately tighter than the Agent Skills standard.
INVOCATION_LIMIT = 64
SKILL_NAME_LIMIT = 40
FILENAME_LIMIT = 60
RELATIVE_PATH_LIMIT = 140
WINDOWS_FULL_PATH_LIMIT = 259  # Excludes the terminating NUL in legacy MAX_PATH.
RESERVED = re.compile(r'^(?:con|prn|aux|nul|com[1-9¹²³]|lpt[1-9¹²³])(?:\.|$)', re.I)


def utf16_units(value):
    """Windows counts supplementary Unicode characters as two code units."""
    return len(str(value).encode('utf-16-le')) // 2


def root_prefix(root):
    """Measure a hypothetical checkout location without resolving or reading it."""
    if root is None:
        return None
    name = str(root)
    if not PurePosixPath(name).is_absolute() and not PureWindowsPath(name).is_absolute():
        raise ValueError('Use an absolute target root for full-path measurements')
    return name if name.endswith(('/', '\\')) else name+'/'


def path_errors(paths, root=None):
    """Check resource names and optional full paths; inputs are file paths."""
    errors, seen = [], {}
    prefix = root_prefix(root)
    for raw in paths:
        name = str(raw)
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts:
            errors.append(f'Non-relative resource path: {name}')
        relative_units = utf16_units(name)
        if relative_units > RELATIVE_PATH_LIMIT:
            errors.append(f'Path has {relative_units} UTF-16 units; repository limit is {RELATIVE_PATH_LIMIT}: {name}')
        filename_units = utf16_units(path.name)
        if filename_units > FILENAME_LIMIT:
            errors.append(f'Filename has {filename_units} UTF-16 units; repository limit is {FILENAME_LIMIT}: {name}')
        if prefix is not None:
            full_units = utf16_units(prefix)+relative_units
            if full_units > WINDOWS_FULL_PATH_LIMIT:
                errors.append(f'Full path has {full_units} UTF-16 units; Windows budget is {WINDOWS_FULL_PATH_LIMIT} at {root}: {name}')
        for index, part in enumerate(path.parts):
            if (RESERVED.match(part) or part.endswith((' ', '.')) or
                    re.search(r'[<>:"\\|?*\x00-\x1f]', part)):
                errors.append(f'Windows-incompatible path component: {name}')
            component_prefix = '/'.join(path.parts[:index + 1])
            key = unicodedata.normalize('NFC', component_prefix).casefold()
            if key in seen and seen[key] != component_prefix:
                errors.append(f'Case/Unicode path collision: {seen[key]} / {component_prefix}')
            seen[key] = component_prefix
    return sorted(set(errors))


def path_report(paths, root):
    """Report measured budgets and the ten longest paths without file access."""
    names = sorted(set(map(str, paths)))
    prefix = root_prefix(root)
    rows = [{'path':name, 'relative_utf16':utf16_units(name),
             'filename_utf16':utf16_units(PurePosixPath(name).name),
             'full_utf16':utf16_units(prefix)+utf16_units(name)} for name in names]
    rows.sort(key=lambda item: (-item['full_utf16'], item['path']))
    return {
        'target_root':str(root), 'root_utf16':utf16_units(root), 'files':len(names),
        'limits':{'skill_name':SKILL_NAME_LIMIT, 'invocation':INVOCATION_LIMIT,
                  'filename_utf16':FILENAME_LIMIT, 'relative_utf16':RELATIVE_PATH_LIMIT,
                  'full_utf16':WINDOWS_FULL_PATH_LIMIT},
        'max_filename_utf16':max((item['filename_utf16'] for item in rows), default=0),
        'max_relative_utf16':max((item['relative_utf16'] for item in rows), default=0),
        'max_full_utf16':max((item['full_utf16'] for item in rows), default=0),
        'checkout_root_budget_utf16':WINDOWS_FULL_PATH_LIMIT-1-RELATIVE_PATH_LIMIT,
        'longest':rows[:10], 'errors':path_errors(names, root),
    }


def skill_name_error(skill):
    if len(skill) > SKILL_NAME_LIMIT:
        return f'Skill name exceeds repository {SKILL_NAME_LIMIT}-character budget: {skill}'
    return None


def invocation_error(plugin, skill):
    qualified = f'{plugin}:{skill}'
    if len(qualified) > INVOCATION_LIMIT:
        return f'Invocation exceeds repository {INVOCATION_LIMIT}-character budget: {qualified}'
    return None
