import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount


# python -m unittest tests/test_investment_account.py


class TestInvestmentAccount(unittest.TestCase):
    # 1 Attributes are set to input values (ensure to test for superclass and subclass attributes)
    def test_init_valid_values(self):
        # Preconditions
        test_account = InvestmentAccount(1, 10, 500.0, date.today(), 2)
    # Expected Result
        excepted = 2.
        actual = test_account._InvestmentAccount__management_fee
    # Method Inputs
        self.assertEqual(excepted, actual)


# 2 management fee has invalid type.


    def test_management_fee_has_invalid_type(self):
        # preconditons
        test_account = InvestmentAccount(1, 10, 500.0, date.today(), "hi")
    # expected result
        expected = 2.5
    # Method Inputs
        actual = test_account._InvestmentAccount__management_fee

        self.assertEqual(expected, actual)

# 3 date created more than 10 years ago
    def test_date_created_more_than_10_years_ago(self):
        # preconditons
        test_account = InvestmentAccount(1, 10, 500.0, date(2000, 1, 1), 2)
        # expected result
        expected = .5
        # Method Inputs
        actual = test_account.get_service_charges()

        self.assertEqual(expected, actual)

# 4 date_created_exactly_10_years_ago.
    def test_date_created_exactly_10_years_ago(self):
        # preconditons
        ten_years = date.today()-timedelta(days=10 * 365.25)
        test_account = InvestmentAccount(
            1, 10, 500.0, date.today()-ten_years, 2)
        # expected result
        expected = 2.5
        # Method Inputs
        actual = test_account.get_service_charges()

        self.assertEqual(expected, actual)

# 5 date_created_within_last_10_years.
    def test_date_created_within_last_10_years(self):
        test_account = InvestmentAccount(1, 10, 500.0, date(2020, 1, 1), 2)
        expected = 2.5
        actual = test_account.get_service_charges()
        self.assertEqual(expected, actual)

# 6 displays_waived_management_fee_when_date_created_more_than_10_years_ago
    def test_displays_waived_management_fee_when_date_created_more_than_10_years_ago(self):
        test_account = InvestmentAccount(1, 10, 500.0, date(2000, 1, 1), 2)
        expected = (f"\nAccount Number: 1  Balance: 500.00$\n"
                    f"Date Created: 2000-01-01 Management Fee: 0.50  Account Type: Investment")
        actual = str(test_account)
        self.assertEqual(expected, actual)

# # 7 displays_management_fee_when_date_created_within_last_10_years
    def test_displays_management_fee_when_date_created_within_last_10_years(self):
        test_account = InvestmentAccount(1, 10, 500.0, date(2020, 1, 1), 2)
        expected = (f"\nAccount Number: 1  Balance: 500.00$\n"
                    f"Date Created: 2020-01-01 Management Fee: 2.50  Account Type: Investment")
        actual = str(test_account)
        self.assertEqual(expected, actual)


# main
if __name__ == "__main__":
    unittest.main()
