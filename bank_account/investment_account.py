"""This module defines the InvestmentAccount class."""

from bank_account import BankAccount
from datetime import date, timedelta

__author__ = "Pablo Raymundo"
__version__ = "1.1.1"


class InvestmentAccount(BankAccount):
    """
    Represents an investment bank account.

    An InvestmentAccount applies a management fee in addition to the base service charge unless the account is older than 10 years.
    """
    TEN_YEARS_AGO = date.today()-timedelta(days=10 * 365.25)

    def __init__(self, account_number, client_number, balance, date_created, management_fee: float):
        """
        Initialize an InvestmentAccount obj.

        account_number: (int) account number.
        client_number: (int) client number.
        balance: (float) balance.
        date_created: (dateClass) date the account was created.
        management_fee: (float) management fee applied to the account.
                    defaults to 2.5 if an invalid value is provided.
        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            management_fee = float(management_fee)
            if (management_fee < 0):
                raise Exception
            self.__management_fee = management_fee
        except Exception:
            self.__management_fee = 2.5

    def __str__(self):
        """
        Return a str of the InvestmentAccount.

        :return: (string) contains investment account attributes
        """

        return (f"\nAccount Number: {self._BankAccount__account_number}  Balance: {self._BankAccount__balance:.2f}$\n"
                f"Date Created: {self._date_created} Management Fee: {(self.get_service_charges()):.2f}  Account Type: Investment")

    def get_service_charges(self) -> float:
        """
        calculate the service charges for the investment account.

        If the account is older than 10 years, only the base service charge is applied.
        Otherwise, the base service charge plus the management fee is applied.

        :return: (float) total service charge.
        """
        if (self._date_created <= self.TEN_YEARS_AGO):
            return self.BASE_SERVICE_CHARGE
        else:
            return (self.BASE_SERVICE_CHARGE+self.__management_fee)
