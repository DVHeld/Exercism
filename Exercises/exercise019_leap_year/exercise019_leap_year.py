"""Leap Year exercise"""

def leap_year(year):
    """Determines if it's a leap year.
 
    :param year: int - The year to check.
 
    :return: bool - True if it's a leap year, False otherwise.
    """

#   Variables for readability:
#   --------------------------

    year_div_100        = year % 100 == 0                       #Is the year divisible by 100?      = A
    year_not_div_100    = year % 100 != 0 # = not year_div_100  #Is the year not divisible by 100?  = B = ¬A
    year_div_400        = year % 400 == 0                       #Is the year divisible by 400?      = C => A
    year_div_4          = year % 4   == 0                       #Is the year divisible by 4?        = D

#   This solution is made to be very readable and easy to follow:
#   =============================================================

    is_century_leap     = year_div_400 # 400 is always divisible by 100 #Is it a century leap year? = E = C
    is_regular_leap     = year_div_4      and year_not_div_100          #Is it a regular leap year? = F = B & D = ¬A & D
    is_leap             = is_century_leap or  is_regular_leap           #Is it a leap year?         = G = E | F = C | (B & D) = C | (¬A & D)
    return is_leap

#    Other possible solutions:
#    =========================
#
#    Using 3 if, no logical operators:
#    ---------------------------------
#
#    if year_div_400:           # C
#        return True
#    if year_div_4:             # D
#        if year_not_div_100:   # B = ¬A
#            return True
#    return False
#
#    Using 2 if:
#    -----------
#
#    if year_div_400:                       # E = C
#       return True
#    if year_div_4 and year_not_div_100:    # F = B & D = ¬A & B
#       return True
#    return False
#
#    Using 1 if:
#    -----------
#
#    if (year_div_100 and year_div_400) or (year_div_4 and year_not_div_100):   # G = E | F = C | (B & D) = C | (¬A & D)
#       return True
#    return False
#
#    Same no if:
#    -----------
#
#    return year_div_400 or (year_div_4 and year_not_div_100)                   # G = E | F = C | (B & D) = C | (¬A & D)
#
#    No if, no variables:
#    --------------------
#
#    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))        # G = E | F = C | (B & D) = C | (¬A & D)
