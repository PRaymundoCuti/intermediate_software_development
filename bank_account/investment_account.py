from bank_account import BankAccount
from datetime import date


class InvestmentAccount(BankAccount):
    __TEN_YEARS_AGO = date.today().replace(year=date.today().year-10)

    def __init__(self, account_number, client_number, balance, date_created, management_fee: float):
        super().__init__(account_number, client_number, balance, date_created)
        try:
            management_fee = float(management_fee)
            if (management_fee < 0):
                raise Exception
            self.__management_fee = management_fee
        except Exception:
            self.__management_fee = 2.5

    def __str__(self):
        base_str = super().__str__()
        if (self._BankAccount__date_created <= self.__TEN_YEARS_AGO):
            return (f"{base_str}"
                    f"Date Created: {self._BankAccount__date_created} Management Fee: (waived fee)  Account Type: Investment")
        else:
            return (f"{base_str}"
                    f"Date Created: {self._BankAccount__date_created} Management Fee: ${self.__management_fee:.2f}  Account Type: Investment")

    def get_service_charges(self) -> float:
        BASE_SERVICE_CHARGE = self._BankAccount__BASE_SERVICE_CHARGE

        if (self._BankAccount__date_created <= self.__TEN_YEARS_AGO):
            print(
                f"Chargers: ${BASE_SERVICE_CHARGE:.2f} + (waived fee) = ${BASE_SERVICE_CHARGE:.2f} ")
            return BASE_SERVICE_CHARGE
        else:
            charge = BASE_SERVICE_CHARGE + \
                self.management_fee
            print(
                f"Chargers: ${BASE_SERVICE_CHARGE:.2f}+ ${self.management_fee:.2f}=${charge:.2f}")
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
