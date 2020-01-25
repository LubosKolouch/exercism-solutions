from collections import defaultdict
import re

def count_words(sentence):
    words = defaultdict(int)
    for w in re.split(r',+| +|\n+|\t+|_+',sentence):
        if w == '':
            continue
        w = re.sub(r"'(.*?)'",r'\1', w)
        w = re.sub(r"[\:\,\.]",'',w)
        w = re.sub(r"[!&@$%^]",'',w)
        words[w.lower()] += 1

    return(dict(words))

