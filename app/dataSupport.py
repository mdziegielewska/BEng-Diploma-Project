# count elements in a file
def count(d, s):
    c = 0
    if isinstance(d, dict):
        for k, v in d.items():
            if k == s:
                c += 1
            c += count(v, s)
    elif isinstance(d, list):
        for l in d:
            c += count(l, s)
    return c
