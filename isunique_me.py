def isunique_hashtable(string):
    hash_table = [[] for i in range(len(string))]

    for i in range(len(string)):
        hash_key = hash(string[i]) % len(string)

        if hash_table[hash_key]:
            for j in hash_table[hash_key]:
                if j == string[i]:
                    print("Not unique characters: " + string[i])
        else:
            hash_table[hash_key].append(string[i])

def isunique_set(string):
    print(len(set(string)) == len(string))

def isunique_ascii(string):
    if len(string) > 128:
        print(False)

    char_table = [False] * 128

    for i in string:
        key = ord(i)
        if char_table[key]:
            return print(False)
        else:
            char_table[key] = True
    print(True)

def isunique_dictionary(string):
    char_dict = {}
    for i in string:
        if i in char_dict:
            return print(False)
        else: 
            char_dict[i] = 1
    print(True)

def isunique_sorting(string):
    sorted_string = sorted(string)
    last = None

    for i in sorted_string:
        if i == last:
            return print(False)
        else:
            last = i
    print(True)

isunique_sorting("asdfgdertu")