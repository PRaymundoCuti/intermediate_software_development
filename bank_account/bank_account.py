"""This module defines the BankAccount class."""

from abc import ABC, abstractmethod
from datetime import date, timedelta

__author__ = "Pablo Raymundo"
__version__ = "1.1.1"


class BankAccount(ABC):
    """
    Represents an bank account.

    blueprint of other bankaccount such Savings, Chequing and Investment
    """

    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """
        Initialize an InvestmentAccount obj.

        account_number: (int) account number.
        client_number: (int) client number.
        balance: (float) balance.
        date_created: (dateClass) date the account was created.
                        defaults to date.today() if an invalid value is provided.
        """
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance
        if (isinstance(date_created, date)):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    @abstractmethod
    def __str__(self) -> str:
        """
        Return a str of the BankAccount.

        :return: (string) abstract method
        """

        pass

    @abstractmethod
    def get_service_charges(self, amount: float) -> float:
        """
        Return a float of the BanktAccount.

        :return: (string) abstract method
        """
        pass

    def update_balance(self, amount: float) -> None:
        """
        Add the amount, previusly checked for deposit() and withdraw() methods

        :return: None
        """
        self.__balance += amount

    def deposit(self, amount: float) -> None:
        """
        check that amount is numeric and greather than zero to add it to balance by update_balance()

        :return: None
        """
        try:
            amount = float(amount)
            if (0 > amount):
                raise ValueError("deposit amount lower than 0")
            self.update_balance(amount)
        except TypeError:
            print("deposit amount is not numerical")
        except Exception as e:
            print(e)

    def withdraw(self, amount: float) -> None:
        """
        check that amount is numeric and smaller than amount to rest it to balance by update_balance()

        :return: None
        """
        try:
            amount = float(amount)
            if (self.__balance < amount):
                raise ValueError("balance lower than amount withdraw")
            self.update_balance(-amount)
        except TypeError:
            print("withdraw amount is not numerical")
        except Exception as e:
            print(e)
