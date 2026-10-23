"""Offline authoring validation for Agent Plugins 1.0.0.

Source: https://agent-plugins.org/specification and its published JSON schemas.
This is a package validator, not a client's recovery policy or runtime test.
"""
import ipaddress
from pathlib import Path, PureWindowsPath
import re
from urllib.parse import urlsplit

PLUGIN_SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
MCP_SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json'
METADATA = {'name', 'version', 'description', 'author', 'homepage',
            'repository', 'license', 'keywords'}


def strings(value):
    return isinstance(value, dict) and all(isinstance(v, str) for v in value.values())


def validate_manifest(folder, read_json):
    manifest = read_json(folder/'plugin.json')
    if not isinstance(manifest, dict):
        raise ValueError('plugin.json must be an object')
    if manifest.get('$schema') != PLUGIN_SCHEMA:
        raise ValueError('missing or unsupported Agent Plugins $schema')
    unknown = set(manifest) - METADATA - {'$schema', 'extensions'}
    if unknown:
        raise ValueError('nonstandard plugin.json fields: '+', '.join(sorted(unknown)))
    name = manifest.get('name')
    if (not isinstance(name, str) or not 1<=len(name)<=64 or
            not re.fullmatch(r'(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?', name)):
        raise ValueError('invalid plugin name')
    if name != folder.name:
        raise ValueError('plugin name mismatch')
    for key in ('version', 'description', 'homepage', 'repository', 'license'):
        if key in manifest and not isinstance(manifest[key], str):
            raise ValueError(key+' must be a string')
    if 'author' in manifest:
        author = manifest['author']
        if not strings(author) or set(author)-{'name', 'email', 'url'}:
            raise ValueError('author must contain only name/email/url strings')
    if 'keywords' in manifest and (not isinstance(manifest['keywords'], list)
            or not all(isinstance(v, str) for v in manifest['keywords'])):
        raise ValueError('keywords must be an array of strings')
    if 'extensions' in manifest:
        extensions = manifest['extensions']
        if not isinstance(extensions, dict) or not all(isinstance(v, dict) for v in extensions.values()):
            raise ValueError('extensions must map namespaces to objects')
        if not all(re.fullmatch(r'[a-z0-9]+(?:[a-z0-9-]*[a-z0-9])?(?:\.[a-z0-9]+(?:[a-z0-9-]*[a-z0-9])?)+', k) for k in extensions):
            raise ValueError('extensions require reverse-domain namespaces')
    claude = read_json(folder/'.claude-plugin/plugin.json')
    if not isinstance(claude, dict):
        raise ValueError('Claude plugin manifest must be an object')
    for key in sorted(METADATA):
        if (key in manifest) != (key in claude) or manifest.get(key) != claude.get(key):
            raise ValueError('portable/Claude manifest drift: '+key)
    mcp = folder/'mcp.json'
    # A dangling manifest link must be rejected, not mistaken for absence.
    if mcp.exists() or mcp.is_symlink():
        validate_mcp(folder, read_json(mcp))
    return manifest


def contained_path(folder, value, field):
    if not value.startswith('./'):
        raise ValueError(field+' must begin with ./')
    relative = value[2:]
    windows = PureWindowsPath(relative)
    if windows.anchor or '..' in windows.parts or '..' in Path(relative).parts:
        raise ValueError(field+' escapes plugin root')
    if any(p.casefold()=='.secret' for p in [*Path(relative).parts, *windows.parts]):
        raise ValueError(field+' uses a protected path')
    target = folder
    for component in ('.', *Path(relative).parts):
        target = target/component
        try:
            info = target.lstat()
        except FileNotFoundError:
            continue
        if target.is_symlink() or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise ValueError(field+' uses a linked package path')
    if not target.resolve().is_relative_to(folder.resolve()):
        raise ValueError(field+' escapes plugin root')


def validate_mcp(folder, mcp):
    if (not isinstance(mcp, dict) or set(mcp)!={'$schema', 'mcpServers'}
            or mcp.get('$schema') != MCP_SCHEMA or not isinstance(mcp.get('mcpServers'), dict)):
        raise ValueError('mcp.json must declare the supported schema and mcpServers object')
    for name, server in mcp['mcpServers'].items():
        label = 'MCP server '+name+': '
        if not isinstance(server, dict):
            raise ValueError(label+'configuration must be an object')
        kind = server.get('type')
        if not isinstance(kind, str):
            raise ValueError(label+'type must be a transport string')
        if kind == 'stdio':
            if set(server)-{'type', 'command', 'args', 'env', 'cwd'}:
                raise ValueError(label+'unknown stdio fields')
            command = server.get('command')
            if not isinstance(command, str) or not command or any(c.isspace() for c in command) or '${' in command:
                raise ValueError(label+'command must be one executable token')
            if command.startswith('./'):
                contained_path(folder, command, label+'command')
            elif any(c in command for c in '/\\:') or command in {'.', '..'}:
                raise ValueError(label+'command must be bare or plugin-relative')
            if 'args' in server and (not isinstance(server['args'], list) or not all(isinstance(v, str) for v in server['args'])):
                raise ValueError(label+'args must be an array of strings')
            if 'env' in server and (not strings(server['env']) or any(k.upper() in {'PLUGIN_ROOT', 'PLUGIN_DATA'} for k in server['env'])):
                raise ValueError(label+'env must contain strings and no reserved plugin variables')
            if 'cwd' in server:
                cwd = server['cwd']
                if not isinstance(cwd, str):
                    raise ValueError(label+'cwd must be a string')
                if cwd == '${PLUGIN_DATA}' or cwd.startswith('${PLUGIN_DATA}/'):
                    if '..' in PureWindowsPath(cwd[len('${PLUGIN_DATA}'):]).parts:
                        raise ValueError(label+'cwd escapes plugin data')
                else:
                    if cwd == '${PLUGIN_ROOT}' or cwd.startswith('${PLUGIN_ROOT}/'):
                        cwd = './'+cwd[len('${PLUGIN_ROOT}'):].lstrip('/')
                    contained_path(folder, cwd, label+'cwd')
        elif kind in {'streamable-http', 'sse'}:
            if set(server)-{'type', 'url', 'headers'} or not isinstance(server.get('url'), str):
                raise ValueError(label+'invalid remote fields')
            if any(c.isspace() or ord(c)<32 for c in server['url']):
                raise ValueError(label+'URL contains whitespace or control characters')
            url = urlsplit(server['url'])
            _ = url.port  # Reject invalid/non-numeric/out-of-range ports.
            try:
                loopback = url.hostname == 'localhost' or ipaddress.ip_address(url.hostname).is_loopback
            except ValueError:
                loopback = False
            if (not url.hostname or url.scheme not in {'http', 'https'} or url.username is not None
                    or url.password is not None or '#' in server['url'] or (url.scheme=='http' and not loopback)):
                raise ValueError(label+'requires HTTPS or loopback HTTP without user information or fragments')
            if 'headers' in server:
                headers = server['headers']
                if not strings(headers) or len({k.casefold() for k in headers}) != len(headers):
                    raise ValueError(label+'headers must be unique fields of strings')
                for key, value in headers.items():
                    if not re.fullmatch(r"[!#$%&'*+.^_`|~0-9A-Za-z-]+", key) or any(ord(c)<32 and c!='\t' or ord(c)==127 or ord(c)>255 for c in value):
                        raise ValueError(label+'invalid HTTP header')
        else:
            raise ValueError(label+'unsupported MCP transport')
