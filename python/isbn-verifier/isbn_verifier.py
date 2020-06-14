def is_valid(isbn):

    result = 0

    pos = 0
    for s in isbn:
        if pos == 9 and s == "X":
            s = 10

        elif ord(s) not in range(ord("0"),ord("9")+1):
            continue

        pos += 1

        if pos > 10:
            return False

        result += (10-pos+1)*int(s)

    if pos != 10:
        return False

    return result % 11 == 0
