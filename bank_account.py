from general_functions import *
class bank_account:
    def __init__(self,account_number,client_number,balance):
        try:
            is_and_greater_than(account_number,"int",0,"account_number")
            is_and_greater_than(client_number,"int",0,"client_number")
            is_and_greater_than(balance,"float",0,"balance")

            self.account_number=account_number
            self.client_number=client_number
            self.balance=balance
        except Exception as e:
            print(f"Error in bank account initialization: {e}")

    def __str__(self) -> str:
        return f" Account number: {self.account_number} Balannce: {self.balance}"
    
    def deposit(self,amount) -> None:
        try:
            is_and_greater_than(amount,"float",0,"amount")
            self.balance+=amount
        except Exception as e:
            print(f"Error in deposit: {e}")

    def withdraw(self,amount) -> None:
        try:
            is_and_greater_than(amount,"float",0,"amount")
            if (amount>self.balance):
                raise ValueError(f"the amount withdraw {amount} is greater than the accounet balance {self.balance}")
            else:
                self.balance-=amount
        except Exception as e:
            print(f"Error in deposit: {e}")