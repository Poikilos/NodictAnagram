import itertools
version = "gas"
for s_tuple in itertools.permutations(version):
    s = ""
    prev_c = None
    for c in s_tuple:
        c_keep = True
        if c == ' ':
            if prev_c == ' ':
                c_keep = False
        if c_keep:
            s += c
        prev_c = c
    print(s)
