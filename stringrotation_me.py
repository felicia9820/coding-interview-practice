def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return print(False)

    first = s1[0]
    idx = s2.index(first)
    res = s2[idx:] + s2[:idx]

    return print(res in s1)

def string_rot_short(s1,s2):
    if len(s1) == len(s2) != 0:
        return print(s2 in s1*2)
    return print(False)

string_rot_short("waterbottle", "erbottlewat")