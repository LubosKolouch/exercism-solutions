""" Exercism task Bookstore """
from collections import Counter


def total(basket):
    """ Compute total discount and amount """

    discounts = {1: 0, 2: 5, 3: 10, 4: 20, 5: 25}
    c = Counter(basket)
    print(c)

    total_sum = 0

    while c:
        round_count = 0
        for x in dict(c):
            round_count += 1

            c[x] -= 1
            if c[x] == 0:
                c.pop(x)

        total_sum +=  round_count *   (8 - 8*discounts[round_count]/100)
        
    return total_sum*100
