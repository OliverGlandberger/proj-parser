import os

def generate_directory_tree(startpath, exclude=None):
    exclude = exclude or []
    paths = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        paths.append('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)

        dirs[:] = [d for d in dirs if d not in exclude and not any(d.endswith(ex) for ex in exclude)]
        files = [f for f in files if f not in exclude and not any(f.endswith(ex) for ex in exclude)]

        for f in files:
            paths.append('{}{}'.format(subindent, f))
    return '\n'.join(paths)
