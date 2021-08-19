def urlify(string):
    result = list(string)
    for i in range(len(result)):
        if result[i] == ' ':
            tail = result[i+1:len(result)-1]
            result[i:i+3] = ['%','2','0']
            result[i+3:] = tail

    string = "".join(result)
    print(string)

def urlify_2(string):
    words = string.split()
    result = ""
    for word in words:
        result += word

        if word != words[len(words)-1]:
            result += '%20'

    print(result)

def urlify_short(string):
    return print(string.strip().replace(" ", '%20'))


urlify_short("Mr John Smith    ")