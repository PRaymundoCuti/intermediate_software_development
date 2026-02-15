"""A program to demonstrate the use of the BankAccount subclasses.
"""
__author__ = "Pablo Raymundo"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount

# 2. Create an instance of a ChequingAccount with values of your
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(1, 1, -100.0, date.today(), -50.0, 0.05)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.
print(str(chequing_account))
chequing_account.get_service_charges()
print(f"\nServices Charges:{chequing_account.get_service_charges()}")

# 4a. Use ChequingAccount instance created in step 2 to deposit
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.
chequing_account.deposit(100)
print(str(chequing_account))
chequing_account.get_service_charges()
print(f"\nServices Charges:{chequing_account.get_service_charges()}")

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(2, 2, 100.0, date.today(), 50.0)


# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.
print(str(savings_account))
print(f"\nServices Charges:{savings_account.get_service_charges()}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw
# enough money from the savings account to cause the balance to fall
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.
savings_account.withdraw(51)
print(str(savings_account))
print(f"\nServices Charges:{savings_account.get_service_charges()}")


print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your
# choice including a date created within the last 10 years.
investment_account = InvestmentAccount(3, 3, 100, date.today(), 5)


# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 8.
print(investment_account)
print(f"\nServices Charges:{investment_account.get_service_charges()}")


# 10. Create an instance of an InvestmentAccount with values of your
# choice including a date created prior to 10 years ago.
investment_account2 = InvestmentAccount(4, 4, 100, date(2010, 1, 1), 5)


# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 10.
print(str(investment_account2))
print(f"\nServices Charges:{investment_account2.get_service_charges()}")


# 12. Update the balance of each account created in steps 2, 5, 8 and 10
# by using the withdraw method of the superclass and withdrawing
# the service charges determined by each instance invoking the
# polymorphic get_service_charges method.
chequing_account.withdraw(chequing_account.get_service_charges())

savings_account.withdraw(savings_account.get_service_charges())

investment_account.withdraw(investment_account.get_service_charges())

investment_account2.withdraw(investment_account2.get_service_charges())

print("===================================================")

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(str(chequing_account))
print(str(savings_account))
print(str(investment_account))
print(str(investment_account2))
