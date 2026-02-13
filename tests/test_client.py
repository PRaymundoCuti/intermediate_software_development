from client.client import Client
p=Client(1,"pablo","raymundo","pr@hotmail.com")
print("p object created")

fail=Client(0,"pablo","raymundo","pr@hotmail.com")
fail=Client("p","pablo","raymundo","pr@hotmail.com")
fail=Client(1," ","raymundo","pr@hotmail.com")
fail=Client(1,"p"," ","pr@hotmail.com")
fail=Client(1,"pablo","raymundo","protmail.com")

print(p.get_client_number())
print(p.get_first_name())
print(p.get_last_name())
print(p.get_email_address())
print(str(p))

## i have to learn to create accessor with propierties and namemingl