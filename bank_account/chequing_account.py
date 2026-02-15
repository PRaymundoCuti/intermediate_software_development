"""This module defines the chequingAccount class."""
from bank_account import BankAccount
from datetime import date

__author__ = "Pablo Raymundo"
__version__ = "1.1.1"


class ChequingAccount(BankAccount):
    """
    Represents an chequing bank account.

    An chequingAccount applies a fee according the amount exceed in the overdraft_limit with a overdraft_rate.
    """

    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit: float, overdraft_rate: float):
        super().__init__(account_number, client_number, balance, date_created)
        """
        Initialize an InvestmentAccount obj.

        account_number: (int) account number.
        client_number: (int) client number.
        balance: (float) balance.
        date_created: (dateClass) date the account was created.
        overdraft_limit: (float) overdraft limit applied to the account.
                    defaults to -100 if an invalid value is provided.
        overdraft_rate: (float) overdraft rate applied to the account.
                    defaults to 2.5 if an invalid value is provided.
        """
        try:
            overdraft_limit = float(overdraft_limit)
            if (overdraft_limit > 0):
                raise Exception
            self.__overdraft_limit = overdraft_limit
        except:
            self.__overdraft_limit = -100

        try:
            overdraft_rate = float(overdraft_rate)
            if (overdraft_rate < 0):
                raise Exception
            self.__overdraft_rate = overdraft_rate
        except Exception:
            self.__overdraft_rate = 0.05

    def __str__(self):
        """        
        Return a str of the InvestmentAccount.

        :return: (string) that contains chequing account attributes
        """
        return (f"\nAccount Number: {self._BankAccount__account_number}  Balance: {self._BankAccount__balance:.2f}$\n"
                f"Overdraft Limit: {self.__overdraft_limit:.2f} Overdraft Rate: {self.__overdraft_rate * 100:.2f}%  Account Type: Chequing")

    def get_service_charges(self) -> float:
        """
        calculate the service charges for the chquing account.

        If the account balance is over the overdraft limit, just basic fee is applied.
        Otherwise, the base balance is below the overdraft limit,the resultant fee would be: the basic fee + exceed * overdraft rate 

        :return: (float) total service charge.
        """
        if (self._BankAccount__balance >= self.__overdraft_limit):
            return self.BASE_SERVICE_CHARGE
        else:
            return (self.BASE_SERVICE_CHARGE-(self._BankAccount__balance-self.__overdraft_limit)*self.__overdraft_rate)

    def withdraw(self, amount) -> None:
        """
        let withdraw amounts greather than the balance in order to attributes overdraft limit and overdraft rate can work

        :return: None
        """
        try:
            amount = float(amount)
            self.update_balance(-1*amount)
        except:
            print("withdraw amount is not numerical")
