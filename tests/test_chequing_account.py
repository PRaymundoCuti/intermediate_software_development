import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

#python -m unittest tests/test_chequing_account.py

class TestChequingAccount(unittest.TestCase):
#1 Attributes are set to input values (ensure to test for superclass and subclass attributes)
    def test_init_valid_values(self):
        person1 = ChequingAccount(1, 10, 500.0, date.today(), -200, 0.1)

        self.assertEqual(person1._BankAccount__balance, 500.0)
        self.assertEqual(person1._ChequingAccount__overdraft_limit, -200.0)
        self.assertEqual(person1._ChequingAccount__overdraft_rate, 0.1)

#2 overdraft limit has invalid type.
    def test_invalid_overdraft_limit(self):
        person2= ChequingAccount(1, 10, 500.0, date.today(), "hi", 0.1)

        self.assertEqual(person2._ChequingAccount__overdraft_limit, -100)

if __name__ == "__main__":
    unittest.main()