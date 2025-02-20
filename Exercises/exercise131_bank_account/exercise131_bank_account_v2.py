"""Bank account exercise"""

from threading import Lock

class BankAccount:
    """A bank account. Stores it's status and balance."""

    def __init__(self):
        self._mutex = Lock()
        self._balance = 0
        self._open = False

    def get_balance(self):
        """Returns the current balance.
 
        :raises ValueError: Raised when the account is not open.
        :return int: The current balance.
        """

        with self._mutex:
            if not self._open:
                raise ValueError('account not open')

            return self._balance

    def open(self):
        """Opens the account.
 
        :raises ValueError: Raised when the account is already open.
        """

        with self._mutex:
            if self._open:
                raise ValueError("account already open")

            self._open = True

    def deposit(self, amount):
        """Adds the given amount to the balance.
 
        :param int amount: The amount of the deposit.
        :raises ValueError: Raised when the account is not open.
        :raises ValueError: Raised when there is no amount input.
        :raises TypeError: Raised when the amount is not an integer.
        :raises ValueError: Raised when the amount is not greater than zero.
        """

        with self._mutex:
            if not self._open:
                raise ValueError('account not open')
            if amount is None:
                raise ValueError("Missing amount input.")
            if not isinstance(amount, int):
                raise TypeError("Amount must be an integer.")
            if amount <= 0:
                raise ValueError('amount must be greater than 0')

            self._balance += amount

    def withdraw(self, amount):
        """Substracts the given amount from the balance.
 
        :param int amount: The amount to be withdrawn.
        :raises ValueError: Raised when the account is not open.
        :raises ValueError: Raised when the amount input is missing.
        :raises TypeError: Raised when the amount input is not an integer.
        :raises ValueError: Raised when the amount is not greater than zero.
        :raises ValueError: Raised when the amount exceeds the current balance.
        """

        with self._mutex:
            if not self._open:
                raise ValueError('account not open')
            if amount is None:
                raise ValueError("Missing amount input.")
            if not isinstance(amount, int):
                raise TypeError("Amount must be an integer.")
            if amount <= 0:
                raise ValueError('amount must be greater than 0')
            if amount > self._balance:
                raise ValueError('amount must be less than balance')

            self._balance -= amount

    def close(self):
        """Closes the account.
 
        :raises ValueError: Raised when te account is not open.
        """

        with self._mutex:
            if not self._open:
                raise ValueError('account not open')

            self._open = False
            self._balance = 0
