"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):

    c = Counter(dice)

    if category == ONES:
        return c[1] 

    if category == TWOS:
        return c[2] *2

    if category == THREES:
        return c[3] *3

    if category == FOURS:
        return c[4] *4

    if category == FIVES:
        return c[5] *5

    if category == SIXES:
        return c[6] *6

    if category == FULL_HOUSE:
        print(c.most_common())
        if c.most_common()[0][1] == 3 and c.most_common()[1][1] == 2:
            return c.most_common()[0][0]*c.most_common()[0][1] + c.most_common()[1][0]*c.most_common()[1][1]
        else:
            return 0


    if category == FOUR_OF_A_KIND:
        for x, v in c.items():
            if v >= 4:
                return x*4

        return 0

    if category == LITTLE_STRAIGHT:
        if sorted(c.keys()) == [1,2,3,4,5]:
            return 30
        else:
            return 0

    if category == BIG_STRAIGHT:
        if sorted(c.keys()) == [2,3,4,5,6]:
            return 30
        else:
            return 0

    if category == CHOICE:
        return sum(dice)

    # YACHT
    if len(c) == 1:
        return 50

    return 0
