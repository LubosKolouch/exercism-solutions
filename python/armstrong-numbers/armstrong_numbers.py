def is_armstrong_number(number):
    sum = 0

    for what in str(number):
        sum += int(what) ** len(str(number))

    return True if sum == number else False
