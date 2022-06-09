from modules.account import Account
from modules.bank import Bank
from modules.owner import Owner


chase = Bank()

# Manual creation of accounts testing

# # # chase.add_account(Account(Owner(12, "Tim", "23rd Street" ), 123, 600))
# chase.add_account(Account(123, 600, account_details = Owner(12, "Tim", "23rd Street")))
# # print(chase.check_balance(123))
# # print(chase.withdraw_money(123, 700))
# # print(chase.deposit_money(123, 100))
# # chase.add_account(Account(Owner(13, "Brad", "99 Street"), 321, -100))
# # print(f"{chase.accounts[0].account_details.name} has an account balance of {chase.accounts[0].balance}!")
# chase.add_account(Account(321, 400))
# print(chase.accounts[0].balance)
# print(chase.accounts[0].account_details.owner_id)
# chase.add_ownership(321, 15, "Tim", "23rd Street")
# # print(chase.accounts[0].account_details.name)
# print(f"{chase.accounts[0].account_details.name} has an account balance of {chase.accounts[0].balance}!")

# Automatic testing of accounts
print(chase.accounts)
print(chase.all_accounts())
print(chase.accounts)
print(chase.accounts[0].id)
# print(chase.accounts[0].balance)