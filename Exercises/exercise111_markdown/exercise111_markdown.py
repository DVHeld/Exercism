"""Markdown exercise"""

import re

def parse(markdown):

    html = ''
    in_list = False
    for line in markdown.split('\n'):
        parsed_line = line
        if re.match('###### (.*)', parsed_line) is not None:
            parsed_line = '<h6>' + parsed_line[7:] + '</h6>'
        elif re.match('##### (.*)', parsed_line) is not None:
            parsed_line = '<h5>' + parsed_line[6:] + '</h5>'
        elif re.match('#### (.*)', parsed_line) is not None:
            parsed_line = '<h4>' + parsed_line[5:] + '</h4>'
        elif re.match('### (.*)', parsed_line) is not None:
            parsed_line = '<h3>' + parsed_line[4:] + '</h3>'
        elif re.match('## (.*)', parsed_line) is not None:
            parsed_line = '<h2>' + parsed_line[3:] + '</h2>'
        elif re.match('# (.*)', parsed_line) is not None:
            parsed_line = '<h1>' + parsed_line[2:] + '</h1>'
        list_item_match = re.match(r'\* (.*)', parsed_line)
        if list_item_match:
            parsed_line = '<li>' + list_item_match.group(1) + '</li>'
            if not in_list:
                in_list = True
                parsed_line = '<ul>' + parsed_line
        if not re.match('<[u?l|h]', parsed_line):
            parsed_line = '<p>' + parsed_line + '</p>'
        bold_match = re.match('(.*)__(.*)__(.*)', parsed_line)
        if bold_match:
            parsed_line = bold_match.group(1) + '<strong>' + bold_match.group(2) + '</strong>' +\
                          bold_match.group(3)
        italics_match = re.match('(.*)_(.*)_(.*)', parsed_line)
        if italics_match:
            parsed_line = italics_match.group(1) + '<em>' + italics_match.group(2) + '</em>' +\
                          italics_match.group(3)
        if in_list and not list_item_match:
            parsed_line = '</ul>' + parsed_line
            in_list = False
        html += parsed_line
    if in_list:
        html += '</ul>'
    return html
