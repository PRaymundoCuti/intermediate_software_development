from bank_account import BankAccount
from datetime import date


class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.0

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
        return (f"\nAccount Number: {self._BankAccount__account_number}  Balance: {self._BankAccount__balance}$\n"
                f"Minimum Balance: {self.__minimun_balance}  Account Type: Savings")

    def get_service_charges(self) -> float:
        if (self._BankAccount__balance >= self.__minimun_balance):
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
