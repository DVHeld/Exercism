"""ETL exercise"""

def transform(legacy_data):
    """Transforms data from the legacy format to the new format.
 
    :param dict legacy_data: The data in the legacy format.
    :return dict: The data in the new format.
    """

    new_data = {}

    for score, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.casefold()] = score    
    return new_data
