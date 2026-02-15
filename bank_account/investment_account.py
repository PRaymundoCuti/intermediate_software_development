from bank_account import BankAccount
from datetime import date, timedelta


class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO = date.today()-timedelta(days=10 * 365.25)

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

        return (f"\nAccount Number: {self._BankAccount__account_number}  Balance: {self._BankAccount__balance:.2f}$\n"
                f"Date Created: {self._date_created} Management Fee: {(self.get_service_charges()):.2f}  Account Type: Investment")

    def get_service_charges(self) -> float:
        if (self._date_created <= self.TEN_YEARS_AGO):
            return self.BASE_SERVICE_CHARGE
        else:
            return (self.BASE_SERVICE_CHARGE+self.__management_fee)
