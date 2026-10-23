#!/usr/bin/env python3
"""Validate, document, and package the canonical skills without installing them."""
import argparse
import hashlib
import json
import os
import posixpath
from pathlib import Path, PureWindowsPath
import re
import runpy
import stat
import subprocess
import sys
import zipfile
try:
    import yaml
except ImportError:
    raise SystemExit('Install the validator dependency: python3 -m pip install -r scripts/requirements.txt')
ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', '.secret', '__pycache__', 'node_modules', '.venv', 'dist',
        '.local', '.cache', '.pytest_cache', '.mypy_cache', '.ruff_cache',
        'desktop.ini', 'thumbs.db', '.ds_store'}
PORTABLE_SKIP = {'.claude-plugin', '.codex-plugin', '.claude', '.codex', '.agents',
                 '.zcode', '.hermes', '.mcp.json', 'agents', 'commands', 'hooks',
                 'state', 'runtime', 'logs'}
PORTABLE_PRIVATE = {'.claude-plugin', '.codex-plugin', '.claude', '.codex', '.agents',
                    '.zcode', '.hermes', '.mcp.json', 'state', '.state', 'runtime', 'logs'}

class FrontmatterLoader(yaml.SafeLoader):
    """Duplicate fields are ambiguous across skill hosts; reject them."""

def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError('duplicate YAML field: '+str(key))
        result[key] = loader.construct_object(value_node)
    return result

FrontmatterLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def skills():
    return sorted(p for p in safe_files(ROOT/'plugins') if p.name=='SKILL.md' and len(p.relative_to(ROOT/'plugins').parts)==4)

def front(path):
    if unsafe_path(path):
        raise ValueError('Protected or linked skill entrypoint')
    text = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        raise ValueError('missing YAML frontmatter')
    metadata = yaml.load(match.group(1), Loader=FrontmatterLoader)
    if not isinstance(metadata, dict):
        raise ValueError('frontmatter must be a mapping')
    return metadata, text

def is_link(path):
    """lstat never follows Windows junctions or other reparse points."""
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, 'st_file_attributes', 0) & 0x400)

def unsafe_path(path):
    """Check ancestors from the filesystem root before touching descendants."""
    path = Path(path)
    if not path.is_absolute():
        path = Path.cwd()/path
    if any(part.casefold()=='.secret' or part=='..' for part in path.parts):
        return True
    return any(is_link(part) for part in [*reversed(path.parents), path])

def excluded_name(name):
    name = name.casefold()
    return (name in SKIP or name.startswith(('.env', '.~lock.')) or name.endswith('.local')
            or '.local.' in name or name.endswith(('.pyc', '.bak')))

def safe_files(folder, portable=False, reject_links=False, root_adapters=True):
    folder = Path(folder)
    if unsafe_path(folder):
        if reject_links:
            raise ValueError('Protected or linked source path: '+str(folder))
        return
    def walk_error(error):
        raise error
    for base, dirs, files in os.walk(folder, followlinks=False, onerror=walk_error):
        base = Path(base)
        if unsafe_path(base):
            if reject_links:
                raise ValueError('Protected or linked source path: '+str(base))
            dirs[:] = []
            continue
        kept = []
        for name in sorted(dirs):
            if base.name.casefold()=='patches':
                continue  # Ignored CG generated patch runs; keep static files in patches/.
            if excluded_name(name) or (portable and (name.casefold() in PORTABLE_PRIVATE or (root_adapters and base==folder and name.casefold() in PORTABLE_SKIP))):
                continue
            if is_link(base/name):
                if reject_links:
                    raise ValueError('Linked source resources are not supported: '+str(base/name))
                continue
            kept.append(name)
        dirs[:] = kept
        for name in sorted(files):
            p = base/name
            if base.name.casefold()=='reports' and name.casefold().endswith('-drift.md'):
                continue
            if excluded_name(name) or (portable and (name.casefold() in PORTABLE_PRIVATE or (root_adapters and base==folder and name.casefold() in PORTABLE_SKIP))):
                continue
            if is_link(p):
                if reject_links:
                    raise ValueError('Linked source resources are not supported: '+str(p))
                continue
            if p.is_file():
                yield p

def read_json(path):
    if unsafe_path(path):
        raise ValueError('Protected or linked manifest path: '+str(path))
    def unique_fields(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError('duplicate JSON field: '+key)
            value[key] = item
        return value
    def invalid_constant(value):
        raise ValueError('invalid JSON constant: '+value)
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_fields, parse_constant=invalid_constant)

def validate_plugin_manifest(folder):
    return runpy.run_path(str(Path(__file__).with_name('plugin_format.py')))['validate_manifest'](folder, read_json)


def digest(folder):
    h = hashlib.sha256()
    for p in safe_files(folder):
        data=p.read_bytes()
        try:
            data.decode('utf-8')
            if b'\0' not in data:data=data.replace(b'\r\n',b'\n')
        except UnicodeDecodeError:
            pass
        h.update(p.relative_to(folder).as_posix().encode()+b'\0'+data+b'\0')
    return h.hexdigest()

def catalog():
    depts = json.loads((ROOT/'docs/departments.json').read_text(encoding='utf-8'))
    result = []
    for p in skills():
        m, _ = front(p)
        result.append({'plugin':p.parts[-4], 'name':m['name'], 'path':p.relative_to(ROOT).as_posix(),
                       'description':m['description'], 'departments':m['metadata']['departments'],
                       'sha256':digest(p.parent),
                       'shared_scripts_sha256':digest(p.parents[2]/'scripts') if (p.parents[2]/'scripts').exists() else None})
    return depts, result

def render(check=False):
    depts, entries = catalog()
    files = {}
    rows = ['# Skill catalog', '', 'Department labels describe intended users, not verified organizational adoption.', '',
            '| Plugin | Skill | Intended departments |', '|---|---|---|']
    for e in entries:
        rows.append(f"| {e['plugin']} | [{e['name']}](../{e['path']}) | {e['departments']} |")
    files[ROOT/'docs/skill-catalog.md'] = '\n'.join(rows)+'\n'
    files[ROOT/'docs/skill-catalog.json'] = json.dumps(entries,indent=2,ensure_ascii=False)+'\n'
    for plugin, ds in depts.items():
        subset=[e for e in entries if e['plugin']==plugin]
        fp=hashlib.sha256(json.dumps(subset,sort_keys=True).encode()).hexdigest()
        section='\n'.join(['<!-- BEGIN SKILL CATALOG -->','## Departments and portable skills','',
            '**Intended departments:** '+', '.join(ds)+'.','',
            f"**{len(subset)} skills.** [Full catalog](../../docs/skill-catalog.md) · [Cross-platform setup](../../docs/PORTABILITY.md).",'',
            'Skill paths and names below are the current invocation identifiers. Previous names are recorded in the [migration map](../../docs/skill-name-migration.json).','',
            '| Skill | Intended departments |','|---|---|']+
            [f"| [{e['name']}](skills/{Path(e['path']).parent.name}/SKILL.md) | {e['departments']} |" for e in subset]+
            ['', 'Catalog fingerprint: `'+fp+'`.', '<!-- END SKILL CATALOG -->'])
        p=ROOT/'plugins'/plugin/'README.md';t=p.read_text(encoding='utf-8')
        t=re.sub(r'\n?<!-- BEGIN SKILL CATALOG -->.*?<!-- END SKILL CATALOG -->\n?', '\n',t,flags=re.S).rstrip()
        files[p]=t+'\n\n'+section+'\n'
    p=ROOT/'README.md';t=p.read_text(encoding='utf-8'); block='\n'.join(['<!-- BEGIN BUNDLE CATALOG -->','## Department map','',
      'These are intended users of the plugins. PMO means project management; GTM means sales and marketing.','',
      '| Plugin | Intended departments | Skills |','|---|---|---|']+
      [f"| [{pl}](plugins/{pl}/README.md) | {', '.join(ds)} | {sum(e['plugin']==pl for e in entries)} |" for pl,ds in depts.items()]+
      ['',f"**{len(depts)} plugins · {len(entries)} top-level skills.** Nested helper skills are bundled resources, not separate catalog entries.", '',
       '[Browse every skill](docs/skill-catalog.md) · [Name migration](docs/skill-name-migration.json)',
       '', 'Catalog fingerprint: `'+hashlib.sha256(json.dumps(entries,sort_keys=True).encode()).hexdigest()+'`.',
       '<!-- END BUNDLE CATALOG -->'])
    t=re.sub(r'\n?<!-- BEGIN BUNDLE CATALOG -->.*?<!-- END BUNDLE CATALOG -->\n?', '\n',t,flags=re.S).rstrip()
    files[p]=t+'\n\n'+block+'\n'
    stale=[]
    for p,t in files.items():
        if not p.exists() or p.read_text(encoding='utf-8')!=t:
            stale.append(p.relative_to(ROOT).as_posix())
            if not check:p.write_text(t, encoding='utf-8', newline='\n')
    if check and stale:raise ValueError('Documentation out of date: '+', '.join(stale))
    print(('Checked' if check else 'Updated')+f' catalog and READMEs for {len(entries)} skills / {len(depts)} plugins')

def validate(base=None, workspace=None, target_root=None):
    errors=[];seen=set();depts=json.loads((ROOT/'docs/departments.json').read_text(encoding='utf-8'))
    portability=runpy.run_path(str(Path(__file__).with_name('portability.py')))
    for p in sorted(p for p in safe_files(ROOT/'plugins') if p.name=='SKILL.md'):
        try:
            m,t=front(p);name=m.get('name','')
            if not isinstance(name,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64 or name!=p.parent.name:
                raise ValueError('invalid name or directory mismatch')
            problem=portability['skill_name_error'](name)
            if problem:raise ValueError(problem)
            if name in seen:raise ValueError('duplicate skill name')
            seen.add(name)
            if not isinstance(m.get('description'),str) or not m['description'].strip() or not 1<=len(m['description'])<=1024:raise ValueError('description length/type')
            if set(m)-{'name','description','license','compatibility','metadata','allowed-tools'}:raise ValueError('nonstandard frontmatter fields')
            if 'compatibility' in m and (not isinstance(m['compatibility'],str) or not 1<=len(m['compatibility'])<=500):raise ValueError('compatibility length/type')
            if 'allowed-tools' in m and not isinstance(m['allowed-tools'],str):raise ValueError('allowed-tools must be a string')
            if not isinstance(m.get('metadata',{}),dict) or not all(isinstance(k,str) and isinstance(v,str) for k,v in m.get('metadata',{}).items()):raise ValueError('metadata must map strings to strings')
            if 'license' in m and not isinstance(m['license'],str):raise ValueError('license must be a string')
            if not m.get('metadata',{}).get('departments'):raise ValueError('missing departments')
            if len(t.splitlines())>=500:raise ValueError('entrypoint exceeds progressive disclosure limit')
            for q in [p,p.parent/'WORKFLOW.md']:
                if unsafe_path(q):raise ValueError('Protected or linked skill resource: '+q.name)
                if not q.exists():continue
                content=q.read_text(encoding='utf-8')
                if re.search(r'/Users/|/mnt/|/home/|[A-Z]:\\',content):raise ValueError('hardcoded host path in '+q.name)
                for link in re.findall(r'\]\(([^)]+)\)',content):
                    if link.startswith(('references/','scripts/','assets/','WORKFLOW.md')) and not any(v in link for v in ('<','*','{')):
                        target=q.parent/link.split('#')[0]
                        if unsafe_path(target):raise ValueError('Protected or linked bundled resource: '+link)
                        if not target.exists():raise ValueError('broken bundled link: '+link)
        except Exception as e:errors.append(f'{p.relative_to(ROOT)}: {e}')
    for folder in sorted((ROOT/'plugins').iterdir()):
        if folder.name.casefold() in SKIP or unsafe_path(folder) or not folder.is_dir():continue
        if folder.name not in depts:errors.append('Missing department entry: '+folder.name)
        mp=folder/'plugin.json'
        try:
            validate_plugin_manifest(folder)
        except Exception as e:errors.append(f'{mp.relative_to(ROOT)}: {e}')
    errors.extend(portability['path_errors']((p.relative_to(ROOT).as_posix() for p in safe_files(ROOT)), target_root or ROOT))
    for p in skills():
        problem=portability['invocation_error'](p.parts[-4],p.parent.name)
        if problem:errors.append(problem)
    if errors:raise ValueError('\n'.join(errors))
    routing=runpy.run_path(str(Path(__file__).with_name('workspace_paths.py')))['audit'](ROOT,workspace)
    if routing['findings']:
        raise ValueError('Workspace routing errors:\n'+'\n'.join(f"{x['file']}:{x['line']}: {x['code']}: {x['reference']}" for x in routing['findings']))
    # Generated thinking-framework blocks/references must match their single source.
    if (ROOT/'docs/thinking-frameworks/skill-map.json').exists():
        runpy.run_path(str(Path(__file__).with_name('thinking_frameworks.py')))['sync'](ROOT,check=True)
    render(check=True)
    if base:
        subprocess.run(['git','rev-parse','--verify',base+'^{commit}'],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
        if base == 'HEAD':
            # Status handles staged, unstaged and untracked files without hydrating historical blobs.
            raw=subprocess.check_output(['git','status','--porcelain=v1','-z','--no-renames','--untracked-files=all'],cwd=ROOT,text=True)
            changed={item[3:] for item in raw.split('\0') if item}
        else:
            changed=set(subprocess.check_output(['git','diff','--no-renames','--name-only',base,'--'],cwd=ROOT,text=True,timeout=60).splitlines())
            changed.update(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines())
        affected={s.split('/')[1] for s in changed if s.startswith('plugins/') and ('/skills/' in s or '/scripts/' in s)}
        required={'README.md'}|{f'plugins/{pl}/README.md' for pl in affected if (ROOT/'plugins'/pl).exists()}
        if affected and not required<=changed:raise ValueError('Skill changes require README updates: '+', '.join(sorted(required-changed)))
    print(f'PASS: {len(seen)} skill entrypoints (including nested helpers), names, metadata, entrypoint paths, bundled links, workspace routing, manifests and README fingerprints')

def report_paths(target_root=None, as_json=False):
    portability=runpy.run_path(str(Path(__file__).with_name('portability.py')))
    report=portability['path_report']((p.relative_to(ROOT).as_posix() for p in safe_files(ROOT)), target_root or ROOT)
    if as_json:
        print(json.dumps(report,indent=2,ensure_ascii=False))
    else:
        print(f"Measured {report['files']} files at {report['target_root']}")
        print(f"Longest path: {report['max_relative_utf16']} relative / {report['max_full_utf16']} full UTF-16 units; longest filename: {report['max_filename_utf16']}")
        print(f"Budgets: 140 relative, 60 filename, 259 full; checkout roots up to {report['checkout_root_budget_utf16']} UTF-16 units fit the repository path budget")
        for row in report['longest']:
            print(f"{row['full_utf16']:3} full / {row['relative_utf16']:3} relative: {row['path']}")
        for problem in report['errors']:
            print(problem)
    return report

def output_directory(output):
    dest = Path(output)
    windows = PureWindowsPath(output)
    if dest.is_absolute() or windows.anchor:
        raise ValueError('Use a relative output directory')
    if any(part.casefold()=='.secret' for part in [*dest.parts, *windows.parts]):
        raise ValueError('Protected output path')
    if '..' in dest.parts or '..' in windows.parts:
        raise ValueError('Output traversal is not supported')
    if unsafe_path(dest):
        raise ValueError('Symlink/junction output paths are not supported')
    absolute = Path.cwd()/dest
    if absolute.is_relative_to(ROOT/'plugins'):
        raise ValueError('Output must stay outside plugin source directories')
    return dest

def write_archive(target, entries):
    names = [entry[0] for entry in entries]
    if len(names)!=len(set(names)):
        raise ValueError('Duplicate resource in archive')
    if target.exists() or is_link(target):
        raise ValueError('Refusing to overwrite '+str(target))
    # Preflight all resources before creating the ZIP; recheck before each read.
    for _, source, _ in entries:
        if unsafe_path(source):
            raise ValueError('Protected or linked source resource: '+str(source))
    target.parent.mkdir(parents=True, exist_ok=True)
    if unsafe_path(target):
        raise ValueError('Protected or linked output path: '+str(target))
    created = False
    try:
        with zipfile.ZipFile(target, 'x', zipfile.ZIP_DEFLATED) as archive:
            created = True
            for name, source, transform in entries:
                if unsafe_path(source):
                    raise ValueError('Protected or linked source resource: '+str(source))
                if transform is None:
                    # Preserve executable permission bits for bundled Unix helpers.
                    archive.write(source, name)
                else:
                    info = zipfile.ZipInfo.from_file(source, arcname=name)
                    info.compress_type = zipfile.ZIP_DEFLATED
                    archive.writestr(info, transform(source.read_bytes()))
    except Exception:
        if created and not unsafe_path(target):
            target.unlink()
        raise
    print(target)

def export(plugin, name, output):
    # Explicit selection avoids flooding another host with unrelated skills.
    choices=[p for p in skills() if p.parts[-4]==plugin and (name is None or p.parent.name==name)]
    if not choices:raise ValueError('No matching plugin/skill')
    dest=output_directory(output)
    packages=[]
    for p in choices:
        target=dest/(p.parent.name+'.zip')
        if target.exists() or is_link(target):raise ValueError('Refusing to overwrite '+str(target))
        entries=[]
        for f in safe_files(p.parent,portable=True,root_adapters=False):
            entries.append((p.parent.name+'/'+f.relative_to(p.parent).as_posix(),f,None))
        names=[entry[0] for entry in entries]
        if len(names)!=len(set(names)):raise ValueError('Duplicate resource in skill export')
        packages.append((target, entries))
    for target, entries in packages:
        write_archive(target, entries)

def export_plugin(plugin, output):
    # Names are identifiers, never paths, even on a different operating system.
    if not isinstance(plugin,str) or not re.fullmatch(r'(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?',plugin):
        raise ValueError('Invalid plugin selection')
    folder=ROOT/'plugins'/plugin
    if unsafe_path(folder) or not folder.is_dir():
        raise ValueError('No safe matching plugin')
    validate_plugin_manifest(folder)
    dest=output_directory(output)
    target=dest/(plugin+'-plugin.zip')
    entries=[]
    doc_names = ('PORTABILITY.md', 'INSTALL.md', 'skill-catalog.md', 'skill-name-migration.json')
    guides = []
    for name in doc_names:
        guide = ROOT / 'docs' / name
        if unsafe_path(guide):
            raise ValueError('Protected or linked package guide')
        if guide.is_file():
            guides.append(guide)
    for f in safe_files(folder,portable=True,reject_links=True):
        relative=f.relative_to(folder).as_posix()
        transform=None
        if f.suffix.lower()=='.md':
            links = {
                ('../../docs/' + g.name).encode('utf-8'):
                posixpath.relpath('docs/' + g.name, posixpath.dirname(relative) or '.').encode('utf-8')
                for g in guides
            }
            def transform(data, replacements=links):
                for previous, current in replacements.items():
                    data = data.replace(previous, current)
                return data
        entries.append((plugin+'/'+relative,f,transform))
    for guide in guides:
        if guide.name == 'skill-catalog.md':
            # An exported child package contains only its own skill rows.
            data = '# Skill catalog\n\n| Skill | Intended departments |\n|---|---|\n'
            _, rows = catalog()
            for row in rows:
                if row['plugin'] == plugin:
                    path = Path(row['path']).relative_to(Path('plugins') / plugin).as_posix()
                    data += f"| [{row['name']}](../{path}) | {row['departments']} |\n"
            transform = lambda raw, content=data.encode('utf-8'): content
        else:
            transform = None
        entries.append((plugin+'/docs/'+guide.name, guide, transform))
    write_archive(target,entries)


def main():
    ap=argparse.ArgumentParser(description=__doc__);sub=ap.add_subparsers(dest='action',required=True)
    v=sub.add_parser('validate');v.add_argument('--base');v.add_argument('--workspace',type=Path)
    v.add_argument('--target-root',help='Measure full paths at an absolute destination checkout root without accessing it')
    r=sub.add_parser('paths',help='Report portable filename and path budgets without reading resource contents')
    r.add_argument('--target-root',help='Absolute destination checkout root; defaults to the current repository')
    r.add_argument('--json',action='store_true',help='Print a machine-readable report')
    d=sub.add_parser('docs');d.add_argument('--check',action='store_true')
    e=sub.add_parser('export',help='Export selected standalone skill ZIPs with their resources');e.add_argument('--plugin',required=True);e.add_argument('--skill');e.add_argument('--output',required=True)
    p=sub.add_parser('export-plugin',help='Export one complete Agent Plugins v1 package; does not install it')
    p.add_argument('--plugin',required=True);p.add_argument('--output',required=True,help='Relative output directory outside plugin sources')
    a=ap.parse_args()
    try:
        if a.action=='validate':validate(a.base,a.workspace,a.target_root)
        elif a.action=='paths':return 1 if report_paths(a.target_root,a.json)['errors'] else 0
        elif a.action=='docs':render(a.check)
        elif a.action=='export-plugin':export_plugin(a.plugin,a.output)
        else:export(a.plugin,a.skill,a.output)
    except (ValueError,OSError,subprocess.CalledProcessError,subprocess.TimeoutExpired) as e:
        print(str(e),file=sys.stderr);return 1
    return 0
if __name__=='__main__':sys.exit(main())
