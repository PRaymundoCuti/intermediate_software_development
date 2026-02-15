from abc import ABC, abstractmethod
from datetime import date, timedelta

"""_summary_

    Returns:
        _type_: _description_
    """


class BankAccount(ABC):

    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance
        if (isinstance(date_created, date)):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def get_service_charges(self, amount: float) -> float:
        pass

    def update_balance(self, amount: float) -> None:
        self.__balance += amount

    def deposit(self, amount: float) -> None:
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
        try:
            amount = float(amount)
            if (self.__balance < amount):
                raise ValueError("balance lower than amount withdraw")
            self.update_balance(-amount)
        except TypeError:
            print("withdraw amount is not numerical")
        except Exception as e:
            print(e)
