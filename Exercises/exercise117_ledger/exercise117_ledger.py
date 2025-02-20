"""Ledger exercise"""


# -*- coding: utf-8 -*-
from datetime import datetime
# from locale import format_string, setlocale, LC_ALL

class LedgerEntry: #Added setter, getter, __str__ and __repr__ methods.
    def __init__(self, date, description, change):
        self._date = datetime.strptime(date, '%Y-%m-%d')
        self._description = description
        self._change = change

    @property
    def date(self):

        return self._date

    @date.setter
    def date(self, date):

        self._date = date

    @property
    def description(self):

        return self._description

    @description.setter
    def description(self, description):

        self._description = description

    @property
    def change(self):

        return self._change

    @change.setter
    def change(self, change):

        self._change = change

    def __str__(self):

        return f"Date: {self.date.year}-{self.date.month:02}-{self.date.day:02}"+\
               f"| Description: {self.description} | Change: {self.change}"

    def __repr__(self):

        return f"LedgerEntry('{self.date.year}-{self.date.month:02}-{self.date.day:02}'"+\
               f", '{self.description}', {self.change})"

def create_entry(date, description, change): # Moved variable assignment to class init.

    return LedgerEntry(date, description, change)

def format_entries(currency, locale, entries):
    """Formats ledger entries according to the given locale and currency.
 
    Supported currencies are USD and EUR. Supported locales are en_US and nl_NL.
 
    This function has been refactored. The locale and currency specifics are now in a dict. The
    strings are now built using f-strings, especially the table header. The date is now formatted
    using date.strftime. The entries are now sorted instead of searched. The list is now iterated
    over using a for loop instead of looped through with a while and pop. The description is now
    truncated using slicing instead of a per-character iteration, and formatted using f-strings.
    The change is now formatted using the locales dictionary and f-strings.
 
    :param str currency: The currency.
    :param str locale: The locale.
    :param list[LedgerEntry] entries: The ledger entries.
    :return str: The formatted ledger table.
    """

    locales_dict = { # Created locales dictionary
        'en_US': {
            'date':'Date',
            'desc':'Description',
            'chng':'Change',
            'dtfstr':'%m/%d/%Y',
            'negpost':')',
            'currpos':{
                'EUR':'€',
                'USD':'$'
            },
            'currneg':{
                'EUR':'(€',
                'USD':'($'
            }
        },
        'nl_NL': {
            'date':'Datum',
            'desc':'Omschrijving',
            'chng':'Verandering',
            'dtfstr':'%d-%m-%Y',
            'negpost':' ',
            'currpos':{
                'EUR':'€ ',
                'USD':'$ '
            },
            'currneg':{
                'EUR':'€ -',
                'USD':'$ -'
            }
        }
    }

    # setlocale(LC_ALL, f"{locale}.UTF-8")
    table = f"{locales_dict[locale]['date']:<11}| "+\
            f"{locales_dict[locale]['desc']:<26}| "+\
            f"{locales_dict[locale]['chng']:<13}"
    entries = sorted(sorted(sorted(entries,
                key=lambda entry: entry.date),
                key=lambda entry: entry.description),
                key=lambda entry: entry.change)

    for entry in entries:
        table += '\n'
        table += entry.date.strftime(locales_dict[locale]['dtfstr']) + ' | '
        if len(entry.description) > 25:
            table += f"{entry.description[:22]}... | "
        else:
            table += f"{entry.description:<26}| "
        if entry.change < 0:
            change_str = locales_dict[locale]['currneg'][currency]
        else:
            change_str = locales_dict[locale]['currpos'][currency]
        # change_str += format_string("%.2f", abs(entry.change/100), grouping=True)
        change = f"{abs(entry.change/100):,.2f}"
        print(change)
        if locale == "nl_NL":
            change = change.replace(".", "*").replace(",", ".").replace("*", ",")
            print(change)
        change_str += change
        change_str += locales_dict[locale]['negpost'] if entry.change < 0 else ' '
        table += f"{change_str:>13}"
    return table
