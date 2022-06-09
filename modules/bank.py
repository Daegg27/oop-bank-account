from modules.owner import Owner
from modules.account import Account
import csv

class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def withdraw_money(self, account_number, withdraw_amount):
        for i in range(0, len(self.accounts)):
            if account_number == self.accounts[i].id:
                try: 
                    if withdraw_amount > self.accounts[i].balance:
                        raise("You will go negative")
                    else:
                        self.accounts[i].balance -= withdraw_amount
                        return self.accounts[i].balance
                except:
                    print("You will go negative")
                    return self.accounts[i].balance
                
                


    def deposit_money(self, account_number, deposit_amount):
        for i in range(0, len(self.accounts)):
            if account_number == self.accounts[i].id:
                self.accounts[i].balance += deposit_amount
                return self.accounts[i].balance
                
                    
    def check_balance(self, account_number):
        for i in range(0, len(self.accounts)):
            if account_number == self.accounts[i].id:
                return self.accounts[i].balance

    # def add_ownership(self, account_number, owner_id, name, address):
    #     for i in range(0, len(self.accounts)):
    #         if account_number == self.accounts[i].id:
    #             self.accounts[i].account_details = Owner(owner_id, name, address)

    def add_ownership(self, account_number, owner_id, name, address):
        for i in range(0, len(self.accounts)):
            if account_number == self.accounts[i].id:
                self.accounts[i].account_details = Owner(owner_id, name, address)


    def all_accounts():
        with open("/mnt/c/Users/kidha/Desktop/CodePlatoon/Homework_Assignments/oop-bank-accounts/support.accounts.csv", newline = "") as f:
           reader = csv.DictReader(f, fieldnames = (id, initial_balance, transaction_date))
           for row in reader:
               new_account = Account(int(id), int(initial_balance), transaction_date)
               self.account.append(new_account)
        return self.accounts

