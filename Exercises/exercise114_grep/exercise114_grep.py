"""Grep exercise"""

import re

def grep(pattern, flags, files):
    """Searches the specified files for the provided pattern.
 
    The following flags can be specified:
    -n Show the match's line number.
    -l Output only the names of the files that contain matching lines.
    -i Case-insensitive matching.
    -v Collect all lines that fail to match.
    -x Whole line matching.
 
    :param str pattern: The pattern to search for.
    :param str flags: The flags. If no flags are specified, an empty string must be provided.
    :param list[str] files: The files to search in.
    :raises TypeError: Raised when the pattern is not a string.
    :raises TypeError: Raised when the flags are not a string.
    :raises TypeError: Raised when there's no file input.
    :raises TypeError: Raised when the files input is not a list.
    :raises TypeError: Raised when there are files that are not strings.
    :raises ValueError: Raised when the provided file input is an empty string.
    :return str: The result of the search.
    """

    if pattern is None:
        pattern = ""
    if not isinstance(pattern, str):
        raise TypeError("Pattern must be a string.")
    if flags is None:
        flags = ""
    if not isinstance(flags, str):
        raise TypeError("Flags must be a string.")
    if files is None:
        raise TypeError("Missing file input.")
    if not isinstance(files, list):
        raise TypeError("Files input must be a list.")
    for file in files:
        if not isinstance(file, str):
            raise TypeError("Files input must be a string.")
        if file == "":
            raise ValueError("Empty file input.")

    output = ""
    matched_lines = []
    flags_list = flags.replace("-", "").split()
    line_no_flag = "n" in flags_list
    file_name_flag = "l" in flags_list
    casefold_flag = "i" in flags_list
    no_match_flag = "v" in flags_list
    line_match_flag = "x" not in flags_list
    multiple_files_flag = len(files) > 1

    for file in files:
        text = open(file).read()
        lines = text.splitlines()
        search_pattern = r'.*' * line_match_flag\
                       + pattern * (not casefold_flag)\
                       + pattern.casefold() * casefold_flag\
                       + '.*' * line_match_flag
        for line_nr, line in enumerate(lines):
            if bool(re.match(search_pattern, line.casefold() if casefold_flag else line))\
               ^ no_match_flag:
                matched_lines.append((line.replace("\n", ""), line_nr+1, file))
    for matched_line in matched_lines:
        line_numbers = "" + (str(matched_line[1]) + ":") * line_no_flag
        line_output = (matched_line[2] + ":") * multiple_files_flag + line_numbers + matched_line[0]
        output += (line_output + "\n") * (not file_name_flag)\
                + (matched_line[2] + "\n") * (file_name_flag and matched_line[2] not in output)
    return output
