"""Native Hermes entrypoint for the repository's canonical skill collection.

Hermes Git installation discovers plugin.yaml at the repository root. Skills
stay in their original folders so shared scripts and relative resources work.
Only registration occurs here; optional helpers and MCP servers are not run.
"""
from pathlib import Path
import re
import stat

ROOT = Path(__file__).absolute().parent
_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def _is_plain(path, directory=False):
    """Check ancestors before the leaf; never follow links or protected paths."""
    path = Path(path).absolute()
    if any(part.casefold() == ".secret" for part in path.parts):
        return False
    try:
        for component in (*reversed(path.parents), path):
            info = component.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
                return False
            if component != path and not stat.S_ISDIR(info.st_mode):
                return False
    except (OSError, ValueError):
        return False
    return stat.S_ISDIR(info.st_mode) if directory else stat.S_ISREG(info.st_mode)


def _skill_paths(root):
    """Find immediate skill entrypoints only, leaving nested helpers as resources."""
    plugins = Path(root) / "plugins"
    if not _is_plain(plugins, directory=True):
        return []
    found = []
    names = set()
    for plugin in sorted(plugins.iterdir()):
        if not _NAME.fullmatch(plugin.name) or not _is_plain(plugin, directory=True):
            continue
        skills = plugin / "skills"
        if not _is_plain(skills, directory=True):
            continue
        for skill in sorted(skills.iterdir()):
            if not _NAME.fullmatch(skill.name) or not _is_plain(skill, directory=True):
                continue
            entrypoint = skill / "SKILL.md"
            if not _is_plain(entrypoint):
                continue
            if skill.name in names:
                raise ValueError("Duplicate Hermes skill name: " + skill.name)
            names.add(skill.name)
            found.append((skill.name, entrypoint))
    return found


def register(ctx):
    """Register existing skills through Hermes' documented native plugin API."""
    skills = _skill_paths(ROOT)
    if not skills:
        raise RuntimeError("No bundled skills found; install the complete repository.")
    for name, entrypoint in skills:
        ctx.register_skill(name, entrypoint)
