def to_rna(dna_strand):
    """ Convert from DNA to RNA """
    to_replace = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }

    rna_strand = ''

    for c in dna_strand:
        rna_strand += to_replace[c.upper()]

    return rna_strand
