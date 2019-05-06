from test_framework import generic_test

# DONE

def shortest_equivalent_path(path):
    DELIM = '/'
    dirs = []
    is_abs = (path[0] == DELIM)
    for d in path.split(DELIM):
        if d == '' or d == '.': continue
        if d == '..':
            if len(dirs) == 0 and is_abs: raise ValueError(' "/.."" is not defined')
            if len(dirs) >= 1 and dirs[-1] != '..': dirs.pop(); continue
        dirs.append(d)
    p = DELIM.join( dirs )
    if is_abs: return DELIM + p
    else: return p


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
