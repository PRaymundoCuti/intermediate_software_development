import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.bank_account import BankAccount

#python -m unittest tests/test_chequing_account.py

class TestChequingAccount(unittest.TestCase):
#1 Attributes are set to input values (ensure to test for superclass and subclass attributes)
    def test_init_valid_values(self):
        test_account = ChequingAccount(1, 10, 500.0, date.today(), -200, 0.1)

        self.assertEqual(test_account._BankAccount__balance, 500.0)
        self.assertEqual(test_account._ChequingAccount__overdraft_limit, -200.0)
        self.assertEqual(test_account._ChequingAccount__overdraft_rate, 0.1)

#2 overdraft limit has invalid type.
    def test_invalid_overdraft_limit(self):
        test_account= ChequingAccount(1, 10, 500.0, date.today(), "hi", 0.1)
        expected=-100
        actual=test_account._ChequingAccount__overdraft_limit
        self.assertEqual(expected,actual)

#3 overdraft rate has invalid type.
    def test_invalid_overdraft_rate(self):
        test_account= ChequingAccount(1, 10, 500.0, date.today(), -100, "hi")
        expected=.05
        actual=test_account._ChequingAccount__overdraft_rate
        self.assertEqual(expected,actual)

#4 date created has invalid type
    def test_invalid_date(self):
        test_account= ChequingAccount(1, 10, 500.0, "hi", -100, -.05)
        expected=date.today()
        actual=test_account._BankAccount__date_created
        self.assertEqual(expected,actual)

#5 balance greater than overdraft limit
    def test_balance_greater_than_overdraft_limit(self):
        test_account= ChequingAccount(1, 10, -99, date.today(), -100, -.05)
        BASE_SERVICE_CHARGE=test_account._BankAccount__BASE_SERVICE_CHARGE
        expected=BASE_SERVICE_CHARGE
        actual_charge=test_account.get_service_charges()
        actual=actual_charge
        self.assertEqual(expected,actual)

#6 balance less than overdraft limit
    def balance_less_than_overdraft_limit(self):
        test_account= ChequingAccount(1, 10, -500, date.today(), -100, -.05)

        BASE_SERVICE_CHARGE=test_account._BankAccount__BASE_SERVICE_CHARGE
        balance=test_account._BankAccount__balance
        overdraft_limit=test_account._ChequingAccount__overdraft_limit
        overdraft_rate=test_account._ChequingAccount__overdraft_rate

        expected=BASE_SERVICE_CHARGE + (balance-overdraft_limit) * overdraft_rate
        actual_charge=test_account.get_service_charges()
        actual=actual_charge
        self.assertEqual(expected,actual)

#7 balance equal to overdraft limit
    def test_balance_equal_to_overdraft_limit(self):
        test_account= ChequingAccount(1, 10, -99, date.today(), -100, -.05)
        BASE_SERVICE_CHARGE=test_account._BankAccount__BASE_SERVICE_CHARGE
        expected=BASE_SERVICE_CHARGE
        actual_charge=test_account.get_service_charges()
        actual=actual_charge
        self.assertEqual(expected,actual)

#8 appropriate value returned based on attribute values.
    def test_str(self):
        test_account= ChequingAccount(1, 10, -99, date.today(), -100, -.05)
        expected=(f"Account Number: {test_account._BankAccount__account_number}  Balance: {test_account._BankAccount__balance}\n"
                f"Overdraft Limit: ${test_account._ChequingAccount__overdraft_limit:.2f} Overdraft Rate: {test_account._ChequingAccount__overdraft_rate * 10:.2f}% "
        )
        actual=str(test_account)
        self.assertEqual(expected,actual)
  
##main
if __name__ == "__main__":
    unittest.main()