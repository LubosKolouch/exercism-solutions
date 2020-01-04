def square(number):
    if number < 1 or number > 64:
        raise ValueError('Number must be between 1 and 64')

    return 2**(number-1)


def total():
    t = 0
    for i in range(64):
        t += 2**i

    return t
