from collections import Counter

def is_palindrome_permutation_hashtable(string):
    res = {}

    for char in string.lower():
        if char == " ":
            continue
        if char not in res:
            res[char] = 1
        else:
            res[char] += 1

    return print(sum(v % 2 for v in res.values()) <= 1)

def is_palindrome_permutation_counter(string):
    count = Counter(string.replace(" ", "").lower())
    return print(sum(val % 2 for val in count.values()) <= 1)


is_palindrome_permutation_hashtable('Tact Coa')