from datetime import datetime


class Payment:
    def __init__(self, payment_id: str, user_id: str, amount: float):
        self.payment_id = payment_id
        self.user_id = user_id
        self.amount = amount
        self.payment_date = datetime.now()

    def get_payment_details(self) -> dict:
        return {
            "payment_id": self.payment_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "payment_date": self.payment_date
        }
    
