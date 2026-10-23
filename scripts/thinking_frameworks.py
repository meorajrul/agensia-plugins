#!/usr/bin/env python3
"""Materialize per-skill thinking-framework references and SKILL.md blocks from one source.

The canonical cards live in docs/thinking-frameworks/frameworks.json and the
skill-to-framework mapping in docs/thinking-frameworks/skill-map.json. Each mapped
skill receives references/thinking-frameworks.md (only its own cards) and a marked
"Thinking frameworks" block in SKILL.md, so standalone skill exports stay complete.
Unmapped skills are never modified; leftover generated content is reported, not deleted.
"""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'docs/thinking-frameworks'
REF = 'references/thinking-frameworks.md'
START = '<!-- thinking-frameworks:start -->'
END = '<!-- thinking-frameworks:end -->'
BLOCK = re.compile(r'\n*' + re.escape(START) + r'.*?' + re.escape(END) + r'\n*', re.S)
BANNED_HINT_CHARS = ('—', '–', ';')
MAX_PER_SKILL = 6


def load(root):
    base = root / SOURCE
    data = json.loads((base / 'frameworks.json').read_text(encoding='utf-8'))
    mapping = json.loads((base / 'skill-map.json').read_text(encoding='utf-8'))
    return data, mapping


def checked_path(root, path):
    """Refuse symlinks and .secret at every component below the repository root."""
    current = root
    for part in path.relative_to(root).parts:
        current = current / part
        if part.casefold() == '.secret':
            raise ValueError('Refusing excluded path: ' + path.relative_to(root).as_posix())
        if current.is_symlink():
            raise ValueError('Refusing symlink path: ' + path.relative_to(root).as_posix())
    return path


def heading_offset(text, anchor):
    """Character offset of the first matching heading outside fenced code, or None."""
    fence, offset = None, 0
    for line in text.split('\n'):
        f = re.match(r'^\s*(`{3,}|~{3,})', line)
        if f:
            ch = f[1][0]
            fence = ch if fence is None else (None if fence == ch else fence)
        elif fence is None and (line.rstrip() == anchor or line.startswith(anchor + ' ')):
            return offset
        offset += len(line) + 1
    return None


def strip_block(text):
    if START not in text:
        return text
    text = BLOCK.sub('\n\n', text)
    return text.rstrip('\n') + '\n' if text.endswith('\n\n') else text


def label(card, groups):
    origin = card['firm_source'] if card['kind'] == 'firm' and card['firm_source'] else 'General guidance'
    return f"{origin} · {groups[card['group']]['label']}"


def render_block(entries, cards):
    lines = [START, '## Thinking frameworks', '',
             "Use these where they fit the step named. They structure the thinking and never replace this skill's "
             'evidence, authorization, approval or judgement rules. Full cards with steps, pitfalls and sources: '
             f'[thinking frameworks]({REF}).', '']
    lines += [f"- **{cards[e['id']]['name']}.** {e['use']}" for e in entries]
    lines.append(END)
    return '\n'.join(lines)


def render_reference(skill, entries, data, reference_intro=None):
    cards = {c['id']: c for c in data['frameworks']}
    src = data['source']
    if reference_intro is not None and (not isinstance(reference_intro, str) or not reference_intro.strip()):
        raise ValueError('reference_intro must be a non-empty string')
    intro = reference_intro if reference_intro is not None else (
        f"Selected from the {src['title']}. {src['checked']} Apply a framework only where it fits the step named "
        "under In this skill. It never overrides the skill's evidence, authorization, approval or judgement rules.")
    out = [f'# Thinking frameworks for {skill}', '', intro, '']
    for e in entries:
        c = cards[e['id']]
        out += [f"## {c['name']}", '', label(c, data['groups']), '',
                f"**In this skill:** {e['use']}", '',
                f"**What it is:** {c['what']}", '',
                f"**Use it when:** {c['when']}", '',
                '**How it works:**', '']
        out += [(f'{i}. ' if c['ordered_steps'] else '- ') + s for i, s in enumerate(c['steps'], 1)]
        out += ['', f"**Daily habit:** {c['habit']}", '', f"**Example:** {c['example']}", '']
        if c['watch_out']:
            out += [f"**Watch out:** {c['watch_out']}", '']
        out += [f"**Origin:** {c['origin']}", '']
        if c['sources']:
            out += ['**Sources:** ' + ' · '.join(f"[{s['title']}]({s['url']})" for s in c['sources']), '']
    out += ['---', '', f"{src['marks']} Generated from the agensia-plugins framework source. Edit that source, not this file.", '']
    return '\n'.join(out)


def plan(root):
    """Validate the source and return {path: expected_text} for every generated file."""
    data, mapping = load(root)
    cards = {c['id']: c for c in data['frameworks']}
    if len(cards) != len(data['frameworks']):
        raise ValueError('Duplicate framework ids in frameworks.json')
    errors, files, mapped = [], {}, set()
    excluded_plugins = mapping.get('excluded_plugins', {})
    excluded_skills = mapping.get('excluded_skills', {})
    for key, spec in mapping['skills'].items():
        try:
            plugin, skill = key.split('/')
            if plugin in excluded_plugins or key in excluded_skills:
                raise ValueError('skill is excluded from framework mapping')
            entry = checked_path(root, root / 'plugins' / plugin / 'skills' / skill / 'SKILL.md')
            if not entry.is_file():
                raise ValueError('SKILL.md not found')
            entries = spec['frameworks']
            ids = [e['id'] for e in entries]
            if not 1 <= len(ids) <= MAX_PER_SKILL or len(set(ids)) != len(ids):
                raise ValueError(f'needs 1 to {MAX_PER_SKILL} unique frameworks')
            for e in entries:
                if e['id'] not in cards:
                    raise ValueError('unknown framework id ' + e['id'])
                if not e.get('use', '').strip() or any(ch in e['use'] for ch in BANNED_HINT_CHARS):
                    raise ValueError('hint for ' + e['id'] + ' is empty or uses a dash/semicolon')
            text = strip_block(entry.read_text(encoding='utf-8'))
            block = render_block(entries, cards)
            anchor = spec.get('anchor')
            if anchor:
                pos = heading_offset(text, anchor)
                if pos is None:
                    raise ValueError('anchor heading not found: ' + anchor)
                text = text[:pos].rstrip('\n') + '\n\n' + block + '\n\n' + text[pos:]
            else:
                text = text.rstrip('\n') + '\n\n' + block + '\n'
            files[entry] = text
            files[checked_path(root, entry.parent / REF)] = render_reference(skill, entries, data, spec.get('reference_intro'))
            mapped.add(entry.parent)
        except (ValueError, KeyError) as exc:
            errors.append(f'{key}: {exc}')
    for entry in sorted((root / 'plugins').glob('*/skills/*/SKILL.md')):
        if entry.parent in mapped or entry.is_symlink():
            continue
        if (entry.parent / REF).exists() or START in entry.read_text(encoding='utf-8'):
            errors.append(entry.relative_to(root).as_posix() + ': unmapped skill has generated framework content; remove it manually')
    if errors:
        raise ValueError('\n'.join(errors))
    return files


def sync(root=ROOT, check=False):
    root = Path(root).absolute()
    files = plan(root)
    stale = []
    for path, text in files.items():
        if not path.exists() or path.read_text(encoding='utf-8') != text:
            stale.append(path.relative_to(root).as_posix())
            if not check:
                path.parent.mkdir(exist_ok=True)
                path.write_text(text, encoding='utf-8')
    if check and stale:
        raise ValueError('Stale thinking-framework content (run scripts/thinking_frameworks.py): ' + ', '.join(stale))
    return len(files) // 2


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true', help='report stale generated content without writing')
    args = ap.parse_args()
    try:
        print(f"PASS: {sync(check=args.check)} skills {'checked' if args.check else 'synchronized'} for thinking frameworks")
    except (ValueError, OSError, KeyError) as exc:
        raise SystemExit(str(exc))
