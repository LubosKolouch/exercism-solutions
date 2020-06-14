def find_anagrams(word, candidates):

    word = word.lower()
    result = []

    for cand in candidates:
        if cand.lower() == word:
            continue

        if sorted(word) == sorted(cand.lower()):
            result.append(cand)

    return result
