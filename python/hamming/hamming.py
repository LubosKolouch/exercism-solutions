def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("different length")
    else:
        count = 0
        for p, item in enumerate(strand_a):
            if strand_a[p] != strand_b[p]:
                count += 1

        return count



    return 1
