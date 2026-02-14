from bank_account import BankAccount
from datetime import date


class SavingsAccount(BankAccount):
    __SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number, client_number, balance, date_created, minimun_balance: float):
        super().__init__(account_number, client_number, balance, date_created)
        try:
            minimun_balance = float(minimun_balance)
            if (minimun_balance < 0):
                raise Exception
            self.__minimun_balance = minimun_balance
        except Exception:
            self.__minimun_balance = 50

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}"
                f"Minimum Balance: ${self.__minimun_balance} Account Type: Savings")

    def get_service_charges(self) -> float:
        BASE_SERVICE_CHARGE = self._BankAccount__BASE_SERVICE_CHARGE
        if (self._BankAccount__balance >= self.__minimun_balance):
            print(f"Balance: ${self._BankAccount__balance:.2f}\n"
                  f"Minimum Balance: ${self.__minimun_balance}\n"
                  f"Calculated Service Charges = ${BASE_SERVICE_CHARGE}\n")
            return BASE_SERVICE_CHARGE
        else:
            charge = BASE_SERVICE_CHARGE * \
                self.__SERVICE_CHARGE_PREMIUM
            print(f"Balance: ${self._BankAccount__balance:.2f}\n"
                  f"Minimum Balance: ${self.__minimun_balance}\n"
                  f"Calculated Service Charges = ${BASE_SERVICE_CHARGE} * {self.__SERVICE_CHARGE_PREMIUM} = ${charge}")
            return charge

    def update_balance(self, amount: float) -> None:
        try:
            amount = float(amount)
            if (self._BankAccount__balance+amount < 0):
                raise ValueError
            self._BankAccount__balance += amount
        except:
            pass

    def deposit(self, amount: float) -> None:
        try:
            amount = float(amount)
            if (amount < 0):
                raise ValueError
            self._BankAccount__balance += amount
        except:
            pass

    def withdraw(self, amount) -> None:
        try:
            amount = float(amount)
            if (amount < 0):
                raise ValueError
            self._BankAccount__balance -= amount
        except:
            pass
