import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

# python -m unittest tests/test_chequing_account.py


class TestChequingAccount(unittest.TestCase):
    # 1 Attributes are set to input values (ensure to test for superclass and subclass attributes)
    def test_init_valid_values(self):
        # Preconditions
        test_account = ChequingAccount(1, 10, 500.0, date.today(), -200, 0.1)

        # Method Inputs

        self.assertEqual(test_account._BankAccount__balance, 500.0)
        self.assertEqual(
            test_account._ChequingAccount__overdraft_limit, -200.0)
        self.assertEqual(test_account._ChequingAccount__overdraft_rate, 0.1)

# 2 overdraft limit has invalid type.
    def test_invalid_overdraft_limit(self):
        # Preconditions

        test_account = ChequingAccount(1, 10, 500.0, date.today(), "hi", 0.1)
        # Expected Result
        expected = -100
        # Method Input
        actual = test_account._ChequingAccount__overdraft_limit

        self.assertEqual(expected, actual)

# 3 overdraft rate has invalid type.
    def test_invalid_overdraft_rate(self):
        # Preconditions

        test_account = ChequingAccount(1, 10, 500.0, date.today(), -100, "hi")
        # Expected Result
        expected = .05
        # Method Inputs
        actual = test_account._ChequingAccount__overdraft_rate

        self.assertEqual(expected, actual)

# 4 date created has invalid type
    def test_invalid_date(self):
        # Preconditions

        test_account = ChequingAccount(1, 10, 500.0, "hi", -100, .05)
        # Expected Result

        expected = date.today()
        # Method Inputs

        actual = test_account._date_created
        self.assertEqual(expected, actual)

# 5 balance greater than overdraft limit
    def test_balance_greater_than_overdraft_limit(self):
        # Preconditions

        test_account = ChequingAccount(1, 10, -99, date.today(), -100, .05)
        # Expected Result

        expected = .5
        # Method Inputs
        actual = test_account.get_service_charges()
        self.assertEqual(round(expected, 2), actual)

# 6 balance less than overdraft limit
    def test_balance_less_than_overdraft_limit(self):
        # Preconditions

        test_account = ChequingAccount(1, 10, -101, date.today(), -100, .05)
        # Preconditions

        expected = .5+1*.05
        # Method Inputs

        actual = test_account.get_service_charges()
        self.assertEqual(round(expected, 2), actual)

# 7 balance equal to overdraft limit
    def test_balance_equal_to_overdraft_limit(self):
        # Preconditions

        test_account = ChequingAccount(1, 10, -100, date.today(), -100, .05)
        # Expected Result

        expected = .5
        # Method Inputs

        actual = test_account.get_service_charges()
        self.assertEqual(expected, actual)


# 8 appropriate value returned based on attribute values.


    def test_str(self):
        test_account = ChequingAccount(1, 10, -99, date.today(), -100, -.05)
        expected = (f"\nAccount Number: 1  Balance: -99.00$\n"
                    f"Overdraft Limit: -100.00 Overdraft Rate: 5.00%  Account Type: Chequing"
                    )
        actual = str(test_account)
        self.assertEqual(expected, actual)


# main
if __name__ == "__main__":
    unittest.main()
