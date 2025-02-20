"""RNA Transcription"""

def to_rna(dna_strand):
    """The RNA complement of the DNA strand.
 
    Dictionary variant.
 
    :param str dna_strand: The DNA strand to be translated.
    :return str: The translated RNA strand. 
    """

    dna_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna = ""
    for nucleotide in dna_strand:
        rna += dna_rna[nucleotide]
    return rna
