""""A program written to demonstrate the use of the BankAccount and 
Client classes.
"""

from bank_account import BankAccount
from client import Client

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "<your name here>"

def main():
    """The main function."""

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  When exceptions are 
    # 'caught', display the exception message to the console.

    # 1. Code a statement which creates a valid instance of the Client 
    # class.
    # - Use your own unique valid values for the inputs to the class.

    p = Client(1, "Pablo", "Raymundo", "pablo@email.com")


    # 2. Declare a BankAccount object with an initial value of None.
    mybank_account=None

    # 3. Using the bank_account object declared in step 2, code a 
    # statement to instantiate the BankAccount object.
    # - Use any integer value for the BankAccount number.
    # - Use the client_number used to create the Client object in step 1 
    # for the BankAccount's client_number. 
    # - Use a floating point value for the balance.

    mybank_account=BankAccount(2,1,100.)



    # 4. Code a statement which creates an instance of the BankAccount 
    # class.
    # - Use any integer value for the BankAccount number.
    # - Use the client_number used to create the Client object in step 1
    # for the BankAccount's client_number. 
    # - Use an INVALID value (non-float) for the balance.
    
    FAILbank_account=BankAccount(2,1,"h")


    # 5. Code a statement which prints the Client instance created in 
    # step 1. 
    # Code a statement which prints the BankAccount instance created in
    # step 3.

    print(str(p))
    print(str(mybank_account))


    # 6. Attempt to deposit a non-numeric value into the BankAccount 
    # create in step 3. 
    mybank_account.deposit("h")



    # 7. Attempt to deposit a negative value into the BankAccount create
    # in step 3. 
    mybank_account.deposit(-1)


    # 8. Attempt to withdraw a valid amount of your choice from the 
    # BankAccount create in step 3. 
        
    mybank_account.withdraw(101.0)




    # 9. Attempt to withdraw a non-numeric value from the BankAccount 
    # create in step 3. 
    mybank_account.withdraw("h")


    # 10. Attempt to withdraw a negative value from the BankAccount 
    # create in step 3. 
    mybank_account.withdraw(-2)


    # 11. Attempt to withdraw a value from the BankAccount create in 
    # step 3 which exceeds the current balance of the account. 
    mybank_account.withdraw(-1)
 

    # 12. Code a statement which prints the BankAccount instance created
    # in step 3.  
    mybank_account.update_balance(1)


if __name__ == "__main__":
    main()
