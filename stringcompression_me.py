def str_compression(s):
    current = " "
    count = 0
    res = ""

    for c in s:
        if c != current:
            res = res + current + str(count)
            current = c
            count = 1
        else:
            count += 1

    res = (res + current + str(count))[2:]

    return print(s) if len(res) >= len(s) else print(res)

str_compression('aabcccccaaa')

