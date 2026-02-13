from bank_account.bank_account import BankAccount

p=BankAccount(1,1,1.)
print("p object created")
fail=BankAccount("f",1,1.)
fail=BankAccount(1,"f",1.)
fail=BankAccount(1,1,"f")


print(p.get_account_number())
print(p.get_client_number())
print(p.get_balance())

p.update_balance(2)
p.update_balance(-1)
p.update_balance("p")

p.deposit(1.)
p.deposit(-1.)
p.withdraw(1.)
p.withdraw(-1.)
p.withdraw(120.)

print(str(p))