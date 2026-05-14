from account import Account

from account import Account
from currentAccount import CurrentAccount

some_account = Account("Ted", "12345678", 1000.00)

some_account.deposit(550.23)
some_account.deposit(100)
some_account.withdraw(50)
# some_account._balance = -800

some_account.balance = 34

some_account.balance = -50

print(some_account.balance)

# my_current_account = CurrentAccount(100, 200)
# my_current_account.deposit(50)
# print(my_current_account.balance)
# my_current_account.withdraw(350)





list = ["banana", "apple", 56]

for item in list:
    if hasattr(item, 'upper'):
        print(item.upper())

if hasattr(some_account, '__str__'):
    val = str(some_account)
    print(val)
if hasattr(some_account, '_balance'):
    val = some_account._balance
    print(val)
if hasattr(some_account, 'deposit'):
    val = some_account.deposit(23)
    print(val)

another = Account(10)

print(Account.numCreated)
print("object another is class",
       another.__class__.__name__)

z = another + some_account
print(z)

some_account.balance = -50
print(some_account.balance)
some_account.balance = 500
print(some_account.balance)
