def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores2 = scores.copy()
    scores2.sort(reverse=True)
    return scores2[:3]
