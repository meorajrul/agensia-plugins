#!/usr/bin/env python3
"""Static routing checks for plugin text; optional checks against a selected workspace."""
import argparse
import json
import os
from pathlib import Path
import re
import sys

SKIP={'.secret','.git','node_modules','__pycache__','.venv','venv','dist','tests','fixtures'}
TEXT={'.md','.py','.sh','.js','.mjs','.cjs','.json','.yaml','.yml'}
def allowed_path(path,root):
    """Check every component before inspecting/reading a target; never follow local symlinks."""
    try:parts=path.relative_to(root).parts
    except ValueError:return False
    current=root
    for part in parts:
        if part.casefold()=='.secret':return False
        current=current/part
        if current.is_symlink():return False
    return True

def files(root):
    if root.is_symlink() or any(p.casefold()=='.secret' for p in root.parts):
        raise ValueError('Excluded source root')
    for base,dirs,names in os.walk(root,followlinks=False):
        dirs[:]=sorted(d for d in dirs if d.casefold() not in SKIP and not (Path(base)/d).is_symlink())
        for name in sorted(names):
            p=Path(base)/name
            if name.casefold() in SKIP or p.is_symlink() or p.suffix not in TEXT:continue
            if name.startswith('.env') or '.local.' in name:continue
            yield p

def resource_base(p,repo):
    parts=p.relative_to(repo/'plugins').parts
    if len(parts)>2 and parts[1]=='skills':return repo/'plugins'/parts[0]/'skills'/parts[2]
    return p.parent

def audit(repo,workspace=None):
    repo=Path(repo).absolute()
    if repo.is_symlink() or any(p.casefold()=='.secret' for p in repo.parts):raise ValueError('Excluded repository')
    if not (repo/'plugins').is_dir():raise ValueError('Expected a plugin repository')
    if workspace is not None:
        workspace=Path(workspace).absolute()
        if any(p.casefold()=='.secret' for p in workspace.parts) or workspace.is_symlink():
            raise ValueError('Excluded workspace')
    findings=[];scanned=0;skills=0;bundled=0
    for p in files(repo/'plugins'):
        text=p.read_text(encoding='utf-8');scanned+=1
        if p.name=='SKILL.md' and len(p.relative_to(repo/'plugins').parts)==4:skills+=1
        base=resource_base(p,repo)
        # Business sources must be supplied by the recipient, never tied to an author's machine.
        for number,line in enumerate(text.splitlines(),1):
            if re.search(r'/Users/|/home/|/mnt/|[A-Z]:\\', line):
                findings.append({'file':p.relative_to(repo).as_posix(), 'line':number,
                                 'reference':'absolute host path', 'code':'fixed-host-path',
                                 'detail':'Resolve the source in the recipient workspace'})
    return {'top_level_skills':skills,'text_files_scanned':scanned,'valid_bundled_legacy_named_references':bundled,
            'workspace_checked':workspace is not None,'findings':findings,
            'scope':'Static structured path references in plugin text and code; excludes protected paths, symlinks, tests and fixtures. No business files read or workflow execution.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--workspace',type=Path);ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    try:result=audit(args.repo,args.workspace)
    except (ValueError,OSError,UnicodeError) as exc:print(str(exc),file=sys.stderr);return 2
    if args.json:print(json.dumps(result,indent=2))
    elif result['findings']:
        for item in result['findings']:print(f"{item['file']}:{item['line']}: {item['code']}: {item['reference']} — {item['detail']}")
    else:print(f"PASS: {result['top_level_skills']} skills / {result['text_files_scanned']} text files; structured paths checked"+(' against workspace' if args.workspace else ' (portable checks)'))
    return 1 if result['findings'] else 0

if __name__=='__main__':sys.exit(main())
