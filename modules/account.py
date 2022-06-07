class Account:

    def __init__(self, id, initial_balance, account_details = None):

        self.id = id
        self.account_details = account_details
        try:
            if initial_balance < 0:
                raise("You need to have some money")
            self.balance = initial_balance
        except:
            print("Add money")