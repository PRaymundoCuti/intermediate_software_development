from .bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):


    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit:float, overdraft_rate:float):
        super().__init__(account_number,client_number, balance, date_created)
        try:
            overdraft_limit=float(overdraft_limit)
            if(overdraft_limit>0):
                raise Exception
            self.__overdraft_limit=overdraft_limit
        except Exception:
            self.__overdraft_limit=-100
            
        try:
            overdraft_rate=float(overdraft_rate)
            if(overdraft_rate<0):
                raise Exception
            self.__overdraft_rate=overdraft_rate
        except Exception:
            self.__overdraft_rate=.05

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f} Overdraft Rate: {self.__overdraft_rate * 10:.2f}% ")

    def get_service_charges(self)->float:
        if self._BankAccount__balance >= self.__overdraft_limit:
            print(f"Chargers: {self._BankAccount__BASE_SERVICE_CHARGE}={self._BankAccount__BASE_SERVICE_CHARGE}")
            return self._BankAccount__BASE_SERVICE_CHARGE
        else:
            charge=self._BankAccount__BASE_SERVICE_CHARGE + (self._BankAccount__balance-self.__overdraft_limit) * self.__overdraft_rate
            print(f"Chargers: {self._BankAccount__BASE_SERVICE_CHARGE}+ ({self._BankAccount__balance}-{self.__overdraft_limit})*{self.__overdraft_rate}={charge:.2f}")
            return charge
        
    
    def update_balance(self,amount:float)->None:
        try:
            amount=float(amount)
            if(self._BankAccount__balance+amount<self.__overdraft_limit):
                raise ValueError
            self._BankAccount__balance+=amount
        except:
            pass
            
    def deposit(self,amount:float)->None:
        try:
            amount=float(amount)
            if(amount<0):
                raise ValueError
            self._BankAccount__balance+=amount
        except:
            pass

    def withdraw(self, amount)->None:
        try:
            amount=float(amount)
            if(amount<0 ):
                raise ValueError
            self._BankAccount__balance-=amount
        except:
            pass

