
from client.general_functions import*
class Client:
    def __init__(self, client_number,first_name,last_name,email_address):
        try:
            is_and_greater_than(client_number,"int",0,"client_number")
            is_name(first_name,"first_name")
            is_name(last_name,"last_name")
            email_verificator(email_address)

            self.client_number=client_number 
            self.first_name=first_name 
            self.last_name=last_name   
            self.email_address=email_address
 
        except Exception as e:
            print(f"Error Iniatilation client: {e}")

    ##accessors
    
    def get_client_number(self)->int:
        return self.client_number
    
    def get_first_name(self)->str:
        return self.first_name
    
    def get_last_name(self)->str:
        return self.last_name
    
    def get_email_address(self)->str:
        return self.email_address
    
    ##str
    def __str__(self)->str:
        return ( f"{self.last_name}, {self.first_name} [{self.client_number}] - {self.email_address}")
    


### extra methods 
##mutators

"""    def set_client_number(self,client_number)->None:
        try:
            is_and_greater_than(client_number,"int",0,"client_number")
            self.client_number=client_number
        except Exception as e:
            print(f"Error Setting client number:{e}")

    def set_first_name(self,first_name)->None:
        try:
            is_name(first_name,"first_name")
            self.first_name=first_name
        except Exception as e:
            print(f"Error Setting client number:{e}")

    def set_last_name(self,last_name)->None:
        try:
            is_name(last_name,"first_name")
            self.first_name=last_name
        except Exception as e:
            print(f"Error Setting client number:{e}")

    def set_email_address(self,email_address)->None:
        try:
            email_verificator(email_address)
            self.email_address=email_address
        except Exception as e:
            print(f"Error Setting client number:{e}")
"""