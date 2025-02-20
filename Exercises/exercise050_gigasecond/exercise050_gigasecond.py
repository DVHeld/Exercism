"""Gigasecond exercise"""

from datetime import datetime, timedelta

def add(moment):
    """Returns the date and time correspondig to one gigasecond after the given
    date and time.
 
    :param datetime moment: The initial date and time.
    :return datetime: The final date and time.
    """

    return moment + timedelta(0,1000000000)
