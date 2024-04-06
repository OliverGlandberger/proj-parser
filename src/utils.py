import os
import fnmatch

def parse_gitignore(gitignore_path):
    exclusions = []
    with open(gitignore_path, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith('#'):
                exclusions.append(stripped_line)
    return exclusions

def is_excluded(path, exclusions):
    for pattern in exclusions:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def generate_directory_tree(startpath, exclude=None, use_gitignore=False):
    exclude = exclude or []
    if use_gitignore:
        gitignore_path = os.path.join(startpath, '.gitignore')
        if os.path.exists(gitignore_path):
            exclude.extend(parse_gitignore(gitignore_path))

    paths = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        paths.append('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)

        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), exclude)]
        files[:] = [f for f in files if not is_excluded(os.path.join(root, f), exclude)]

        for f in files:
            paths.append('{}{}'.format(subindent, f))
    return '\n'.join(paths)
