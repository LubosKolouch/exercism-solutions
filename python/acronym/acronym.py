import re

def abbreviate(words):
    result = ''
    for w in re.split(r' |-|_',words):
        if len(w) == 0: continue
        result += w[0].upper()
    return(result)
