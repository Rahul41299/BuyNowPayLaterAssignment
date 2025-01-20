class User:
    def __init__(self, user_id: str, name: str, credit_limit: float):
        self.user_id = user_id
        self.name = name
        self.credit_limit = credit_limit
        self.available_credit = credit_limit
    
    def get_available_credit(self):
        return self.available_credit

    def update_credit(self, amount: float):
        self.available_credit -= amount
