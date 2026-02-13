from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):

    __BASE_SERVICE_CHARGE = 0.50 

    def __init__(self,account_number:int,client_number:int,balance:float,date_created:date):
        self.__account_number=account_number
        self.__client_number=client_number
        self.__balance=balance
        if(isinstance(date_created,date)):
            self.__date_created=date_created
        else:
            self.__date_created=date.today()

    @abstractmethod
    def update_balance(self)->None:
        pass

    @abstractmethod
    def deposit(self,amount:float)->None:
        pass

    @abstractmethod
    def withdraw(self,amount:float)->None:
        pass


    def __str__(self) -> str:
        return (f"Account Number: {self.__account_number}  Balance: {self.__balance}\n")

    @abstractmethod
    def get_service_charges(self)->float:
        pass