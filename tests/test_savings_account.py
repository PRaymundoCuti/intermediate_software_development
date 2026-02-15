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
        self.assertEqual(expected, round(actual, 2))

# # 3 balance_greater_than_minimum_balance

    def test_balance_greater_than_minimum_balance(self):

        test_account = SavingsAccount(1, 1, 500.0, date(2000, 1, 1), 50)
        expected = 0.5
        actual = test_account.get_service_charges()
        self.assertEqual(expected, actual)

# # 4 balance_equal_to_minimum_balance

    def test_balance_equal_to_minimum_balance(self):
        test_account = SavingsAccount(
            1, 10, 50.0, date.today().replace(year=date.today().year-10), 50)
        expected = .5
        actual = test_account.get_service_charges()
        self.assertEqual(expected, actual, 2)

# # 5 balance_less_than_minimum_balance
    def test_balance_less_than_minimum_balance(self):

        test_account = SavingsAccount(
            1, 10, 40, date.today().replace(year=date.today().year-10), 50)
        expected = .5*2
        actual = test_account.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

# # 6  appropriate_value_returned_based_on_attribute_values.

    def test_appropriate_value_returned_based_on_attribute_values(self):
        test_account = SavingsAccount(1, 10, 500.0, date(2000, 1, 1), 50)
        expected = (f"\nAccount Number: 1  Balance: 500.0$\n"
                    f"Minimum Balance: 50.0  Account Type: Savings")
        actual = str(test_account)
        self.assertEqual(expected, actual)


# main
if __name__ == "__main__":
    unittest.main()
