def is_one_away_hashtable(str1, str2):
    unmatched = {}

    len1 = len(str1)
    len2 = len(str2)

    if (len2 > len1 + 1) or (len2 < len1 - 1):
        return print(False)

    for i in range(len1):
        if str1[i] in unmatched:
            unmatched[str1[i]] += 1
        else:
            unmatched[str1[i]] = 1
       
    for i in range(len2):
        if str2[i] in unmatched:
            unmatched[str2[i]] -= 1

    return print(sum(v for v in unmatched.values()) <= 1)

def is_one_away_correct(str1, str2):
    if len(str1) == len(str2):
        return is_replace(str1, str2)
    if len(str1) + 1 == len(str2):
        return is_insert(str1, str2)
    if len(str1) == len(str2) + 1:
        return is_insert(str2, str1)
    return False

def is_replace(str1, str2):
    edited = False
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            if edited:
                return print(False)
            edited = True
    return print(True)

def is_insert(str1, str2):
    edited = False
    i, j = 0, 0

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if edited:
                return print(False)
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return print(True)


    

is_one_away_correct('pale', 'ple')
is_one_away_correct('pales', 'pale')
is_one_away_correct('pale', 'bale')
is_one_away_correct('pale', 'bake')
