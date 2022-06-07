from modules.owner import Owner
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

    def add_ownership(self, account_number, owner_id, name, address):
        for i in range(0, len(self.accounts)):
            if account_number == self.accounts[i].id:
                self.accounts[i].account_details = Owner(owner_id, name, address)
