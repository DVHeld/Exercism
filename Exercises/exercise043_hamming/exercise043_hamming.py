"""Hamming exercise"""

def distance(strand_a, strand_b):
    """Calculates the Hamming distance between the strands.
 
    :param str strand_a: The first strand.
    :param str strand_b: The second strand.
    :return int: the Hamming distance.
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hamming_distance = 0
    for position, nucleotide in enumerate(strand_a):
        if nucleotide != strand_b[position]:
            hamming_distance += 1
    return hamming_distance
