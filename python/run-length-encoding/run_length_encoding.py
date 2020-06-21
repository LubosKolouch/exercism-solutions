import re

def decode(string):
    
    if string == "":
        return ''

    count = ''
    dec_arr = ''

    for x, char in enumerate(string):
        if char.isdigit():
            count = count + str(char)
        else:
            if count == '':
                count = 1
            for i in range(max(1,int(count))):
                dec_arr += char
            count = ''

    return dec_arr


def encode(string):
    last_char = ''
    result = ''
    count = 0

    for x, char in enumerate(string):

        if char != last_char:

            if last_char != '':
                if count > 1:
                    result += str(count)
                result += last_char
            last_char = char
            count = 1
        else:
            count += 1

    if count > 1:
        result += str(count)
    result += last_char   

    return result
