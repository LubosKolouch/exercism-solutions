def is_pangram(sentence):
    letters = dict()

    for char in sentence:
        letters[char.lower()] = 1

    for x in range(97,123):
        if letters.get(chr(x),0) == 0:
            return False

    return True
