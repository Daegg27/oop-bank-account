class Owner:
    
    # For manual creation of accounts (version 1)
    
    def __init__(self, owner_id, name, address):

        self.owner_id = owner_id
        self.name = name
        self.address = address


    # For automatic creation of accounts with CSV file

    # def __init__(self, owner_id, first_name, last_name, address, city, state):

    #     self.owner_id = owner_id
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.address = address
    #     self.city = city
    #     self.state = state
