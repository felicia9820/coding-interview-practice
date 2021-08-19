from collections import Counter

def ispermutation_set(str1, str2):
    if len(str1) != len(str2):
        return print(False)

    return print(set(str1) == set(str2))


def ispermutation_dictionary(str1, str2):
    if len(str1) != len(str2):
        return print(False)

    char_dict = {}

    for i in str1:
        char_dict[i] = 0

    for i in str2:
        if i in char_dict and char_dict[i] == 0:
            char_dict[i] = 1
        else:
            return print(False)

    if list(char_dict.values()).count(1) == len(str1):
        return print(True)
    else:
        return print(False)

def ispermutation_sorting(str1, str2):
    if len(str1) != len(str2):
        return print(False)

    s1, s2 = sorted(str1), sorted(str2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return print(False)
        else:
            continue
    print(True)

def ispermutation_ascii(str1, str2):
    if len(str1) != len(str2):
        return print(False)

    char_list = [0] * 256

    for i in str1:
        char_list[ord(i)] += 1

    for i in str2:
        if char_list[ord(i)] == 0:
            return print(False)

        char_list[ord(i)] -= 1

    print(True)

def ispermutation_counter(str1, str2):
    if len(str1) != len(str2):
        return print(False)

    return print(Counter(str1) == Counter(str2))

ispermutation_counter("asddfg", "sdfdag")
ispermutation_counter("asdfg", "sdfgh")

