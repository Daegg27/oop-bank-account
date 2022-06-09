class Account:

    # For manual creation of accounts (Version 1)
    
    # def __init__(self, id, initial_balance, account_details = None):

    #     self.id = id
    #     self.account_details = account_details
    #     try:
    #         if initial_balance < 0:
    #             raise("You need to have some money")
    #         self.balance = initial_balance
    #     except:
    #         print("Add money")
    
    # For automatic creation of accounts with CSV file 

    def __init__(self, id, initial_balance, transaction_date):

        self.id = id
        try:
            if initial_balance < 0:
                raise("You need to have some money")
            self.balance = initial_balance
        except:
            print("Add money")
        self.transaction_date = transaction_date