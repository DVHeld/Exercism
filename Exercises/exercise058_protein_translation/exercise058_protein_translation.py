"""Protein Translation exercise"""

TRANSLATIONS = {
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "AUG": "Methionine",
    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",
    "AGU": "Serine",
    "AGC": "Serine",
    "AGA": "Arginine",
    "AGG": "Arginine",
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",
    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "GAU": "Aspartic acid",
    "GAC": "Aspartic acid",
    "GAA": "Glutamine",
    "GAG": "Glutamine",
    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGA": "STOP",
    "UGG": "Tryptophan",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",
    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine"
}

def proteins(strand):
    """Returns the translated proteins corresponding to the provided RNA strand.
 
    :param str strand: The RNA strand to be translated.
    :return list[str]: The translated proteins.
    """

    return [] if not strand or\
                 not isinstance(strand, str) or\
                 TRANSLATIONS[strand[:3]] == "STOP"\
        else [TRANSLATIONS[strand[:3]], *proteins(strand[3:])]
