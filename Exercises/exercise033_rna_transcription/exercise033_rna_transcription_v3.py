"""RNA Transcription"""

def to_rna(dna_strand):
    """The RNA complement of the DNA strand.
 
    If variant.
 
    :param str dna_strand: The DNA strand to be translated.
    :return str: The translated RNA strand. 
    """

    rna = ""
    for nucleotide in dna_strand:
        if nucleotide == "G":
            rna += "C"
        elif nucleotide == "C":
            rna += "G"
        elif nucleotide == "T":
            rna += "A"
        elif nucleotide == "A":
            rna += "U"
    return rna
