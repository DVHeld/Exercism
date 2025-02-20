"""Currency Exchange exercise

Functions for calculating steps in exchanging currency.
 
Python numbers documentation:
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
 
Overview of exchanging currency when travelling:
https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""

def exchange_money(budget, exchange_rate):
    """Exchanges money according to the given exchange rate.
 
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    
    return (1 / exchange_rate) * budget

def get_change(budget, exchanging_value):
    """Remaining money after an exchange.
 
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """Value of the given amount of bills of the given denomination.
 
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    """Amount of bills of the given denomination from the given money amount.
 
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return int(amount / denomination)

def get_leftover_of_bills(amount, denomination):
    """Remaining money amount after getting the money in bills of the given denomination.
 
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Returns the maximum amount of foreign currency obtainable.
 
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    real_exchange_rate = exchange_rate * (1 + (spread / 100))
    exchangeable_amount = (1 / real_exchange_rate) * budget
    number_of_bills = int(exchangeable_amount / denomination)
    return number_of_bills * denomination
