import re
from collections import defaultdict

def is_isogram(string):
    dic = defaultdict(int)
    for c in string:
        if c in " -": continue
        dic[c.lower()] += 1
        if dic[c.lower()] > 1:
            return False

    return True
