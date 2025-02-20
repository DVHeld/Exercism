"""Meetup exercise"""

from datetime import date
from calendar import day_name, Calendar, weekday

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
 
    message: explanation of the error.
    """

    def __init__(self, message):

        self.message = message

def meetup(year, month, week, day_of_week):
    """Calculates the date of the meetup according to the provided parameters.
 
    :param int year: The meetup's year.
    :param int month: The meetup's month.
    :param str week: The meetup's week. Valid values go through 'first' to 'fifth',
                     'last' and 'teenth'.
    :param str day_of_week: The name of the meetup's weekday.
    :raises TypeError: Raised when the year is not an integer.
    :raises TypeError: Raised when the month is not an integer.
    :raises TypeError: Raised when the week is not a string.
    :raises TypeError: Raised when the day of week is not a string.
    :raises ValueError: Raised when the week value is invalid.
    :raises ValueError: Raised when the day of week is invalid.
    :raises ValueError: Raised when the year is invalid.
    :raises ValueError: Raised when the month is invalid.
    :raises MeetupDayException: Raised when the requested day does'nt exist.
    :return date: The meetup's date.
    """

    weeks = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "last": -1, "teenth": -2}

    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")
    if not isinstance(month, int):
        raise TypeError("Month must be an integer.")
    if not isinstance(week, str):
        raise TypeError("Week must be a string.")
    if not isinstance(day_of_week, str):
        raise TypeError("Day of week must be a string.")
    if week not in weeks:
        raise ValueError(f"Invalid week. Valid weeks are: {list(weeks.keys())}.")
    if day_of_week not in day_name:
        raise ValueError(f"Invalid day of week name. Valid names are: {list(day_name)}.")
    if 1 > year > 9999:
        raise ValueError("Invalid year.")
    if 1 > month > 12:
        raise ValueError("Invalid month.")

    count = weeks[week]
    month_iterator = Calendar().itermonthdays(year, month)
    if count == -1:
        count = 1
        month_iterator = reversed(list(month_iterator))
    elif count == -2:
        count = 1
        while next(month_iterator) < 12:
            continue
    while count:
        try:
            day = next(month_iterator)
        except Exception as exc:
            raise MeetupDayException("That day does not exist.") from exc
        if not day:
            continue
        if day_name[weekday(year, month, day)] == day_of_week:
            count -= 1
    return date(year, month, day)
