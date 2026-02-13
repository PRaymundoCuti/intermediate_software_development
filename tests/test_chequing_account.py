import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount


class TestChequingAccount(unittest.TestCase):

    def test_init_valid_values(self):
        person1 = ChequingAccount(1, 10, 500.0, date.today(), -200, 0.1)

        self.assertEqual(person1._BankAccount__balance, 500.0)
        self.assertEqual(person1._ChequingAccount__overdraft_limit, -200.0)
        self.assertEqual(person1._ChequingAccount__overdraft_rate, 0.1)

if __name__ == "__main__":
    unittest.main()