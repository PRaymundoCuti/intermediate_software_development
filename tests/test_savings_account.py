import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount


# python -m unittest tests/test_savings_account.py


class TestSavingsAccount(unittest.TestCase):
    # 1 Attributes are set to input values (ensure to test for superclass and subclass attributes)
    def test_init_valid_values(self):
        # Preconditions
        test_account = SavingsAccount(1, 10, 500.0, date.today(), 2)
    # Expected Result
        excepted = 2.
        actual = test_account._SavingsAccount__minimun_balance
    # Method Inputs
        self.assertEqual(excepted, actual)


# # 2 minimum_balance_has_invalid_type

    def test_minimum_balance_has_invalid_type(self):
        test_account = SavingsAccount(1, 10, 500.0, date.today(), "hi")
        expected = 50
        actual = test_account._SavingsAccount__minimun_balance
        self.assertEqual(expected, actual)

# # 3 balance_greater_than_minimum_balance

    def test_balance_greater_than_minimum_balance(self):

        test_account = SavingsAccount(1, 1, 500.0, date(2000, 1, 1), 50)
        expected = test_account._BankAccount__BASE_SERVICE_CHARGE
        actual = test_account.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

# # 4 balance_equal_to_minimum_balance

    def test_balance_equal_to_minimum_balance(self):
        test_account = SavingsAccount(
            1, 10, 50.0, date.today().replace(year=date.today().year-10), 50)
        expected = test_account._BankAccount__BASE_SERVICE_CHARGE
        actual = test_account.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

# # 5 balance_less_than_minimum_balance
    def test_balance_less_than_minimum_balance(self):
        test_account = SavingsAccount(
            1, 10, 40, date.today().replace(year=date.today().year-10), 50)
        expected = test_account._BankAccount__BASE_SERVICE_CHARGE * \
            test_account._SavingsAccount__SERVICE_CHARGE_PREMIUM
        actual = test_account.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

# # 6  appropriate_value_returned_based_on_attribute_values.

    def test_appropriate_value_returned_based_on_attribute_values(self):
        test_account = SavingsAccount(1, 10, 500.0, date(2000, 1, 1), 50)
        expected = (f"Account Number: {test_account._BankAccount__account_number}  Balance: {test_account._BankAccount__balance}$\n"
                    f"Minimum Balance: ${test_account._SavingsAccount__minimun_balance} Account Type: Savings")
        actual = str(test_account)
        self.assertEqual(expected, actual)


# main
if __name__ == "__main__":
    unittest.main()
