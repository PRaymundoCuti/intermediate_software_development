import unittest
from datetime import date
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


# # 2 management fee has invalid type.


    def test_management_fee_has_invalid_type(self):
        test_account = InvestmentAccount(1, 10, 500.0, date.today(), "hi")
        expected = 2.5
        actual = test_account._InvestmentAccount__management_fee
        self.assertEqual(expected, actual)

# # 3 date created more than 10 years ago

    def test_date_created_more_than_10_years_ago(self):
        test_account = InvestmentAccount(1, 10, 500.0, date(2000, 1, 1), 2)
        expected = test_account._BankAccount__BASE_SERVICE_CHARGE
        actual = test_account.get_service_charges()
        self.assertEqual(expected, actual)

# # 4 date_created_exactly_10_years_ago.
    def test_date_created_exactly_10_years_ago(self):
        test_account = InvestmentAccount(
            1, 10, 500.0, date.today().replace(year=date.today().year-10), 2)
        expected = test_account._BankAccount__BASE_SERVICE_CHARGE

        actual = test_account.get_service_charges()
        self.assertEqual(expected, actual)

# # 5 date_created_within_last_10_years.
    def test_date_created_within_last_10_years(self):
        test_account = InvestmentAccount(1, 10, 500.0, date(2000, 1, 1), 2)
        expected = test_account._BankAccount__BASE_SERVICE_CHARGE
        actual = test_account.get_service_charges()
        self.assertEqual(expected, actual)

# # 6 displays_waived_management_fee_when_date_created_more_than_10_years_ago
    def test_displays_waived_management_fee_when_date_created_more_than_10_years_ago(self):
        test_account = InvestmentAccount(1, 10, 500.0, date(2000, 1, 1), 2)
        expected = (f"Account Number: {test_account._BankAccount__account_number}  Balance: {test_account._BankAccount__balance}$\n"
                    f"Date Created: {test_account._BankAccount__date_created} Management Fee: (waived fee)  Account Type: Investment")
        actual = str(test_account)
        self.assertEqual(expected, actual)

# # 7 displays_management_fee_when_date_created_within_last_10_years
    def test_displays_management_fee_when_date_created_within_last_10_years(self):
        test_account = InvestmentAccount(1, 10, 500.0, date(2020, 1, 1), 2)
        expected = (f"Account Number: {test_account._BankAccount__account_number}  Balance: {test_account._BankAccount__balance}$\n"
                    f"Date Created: {test_account._BankAccount__date_created} Management Fee: ${test_account._InvestmentAccount__management_fee:.2f}  Account Type: Investment")
        actual = str(test_account)
        self.assertEqual(expected, actual)


# main
if __name__ == "__main__":
    unittest.main()
