"""This module defines the SavingAccount class."""


from bank_account import BankAccount
from datetime import date

__author__ = "Pablo Raymundo"
__version__ = "1.1.1"


class SavingsAccount(BankAccount):
    """
    Represents an savings bank account.

    An SevingsAccount applies a fee according if balance is below the minimun balance
    """
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number, client_number, balance, date_created, minimun_balance: float):
        super().__init__(account_number, client_number, balance, date_created)
        """
        Initialize an InvestmentAccount obj.

        account_number: (int) account number.
        client_number: (int) client number.
        balance: (float) balance.
        date_created: (dateClass) date the account was created.
        minimun_balance: (float) minimun balance.
                    defaults to 50 if an invalid value is provided.
        """
        try:
            minimun_balance = float(minimun_balance)
            if (minimun_balance < 0):
                raise Exception
            self.__minimun_balance = minimun_balance
        except Exception:
            self.__minimun_balance = 50

    def __str__(self):
        """
        Return a str of the SavingsAccount.

        :return: (string) contains investment account attributes
        """

        return (f"\nAccount Number: {self._BankAccount__account_number}  Balance: {self._BankAccount__balance}$\n"
                f"Minimum Balance: {self.__minimun_balance}  Account Type: Savings")

    def get_service_charges(self) -> float:
        """ calculate the service charges for the savings account.

        If the account balance is greather than minimun balance, just base_service charge is applied.
        Otherwise, the base service charge * service charge premium .

        :return: (float) total service charge.
        """

        if (self._BankAccount__balance >= self.__minimun_balance):
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
