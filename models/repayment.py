from datetime import datetime, timedelta
from typing import List

class RepaymentPlan:
    def __init__(self, user_id: str, purchase_id: str, total_amount: float):
        self.user_id = user_id
        self.purchase_id = purchase_id
        self.total_amount = total_amount
        self.remaining_balance = total_amount
    
    def calculate_outstanding_balance(self):
        return self.remaining_balance
    
    def update_payment(self, amount: float):
        self.remaining_balance -= amount
        return self.remaining_balance

    def get_plan_details(self):
        return {
            "user_id": self.user_id,
            "purchase_id": self.purchase_id,
            "total_amount": self.total_amount,
            "remaining_balance": self.remaining_balance
        }

class FixedPaymentPlan(RepaymentPlan):
    def __init__(self, user_id, purchase_id, total_amount):
        super().__init__(user_id, purchase_id, total_amount)

    def pay_full_amount(self):
        self.remaining_balance = 0
        return {"status": "Paid", "remaining_balance": self.remaining_balance}

class EMIPlan(RepaymentPlan):
    def __init__(self, user_id, purchase_id, total_amount, interest_rate: float, tenure_months: int, late_fee: float):
        super().__init__(user_id, purchase_id, total_amount)
        self.interest_rate = interest_rate
        self.tenure_months = tenure_months
        self.late_fee = late_fee
        self.monthly_installment = self.calculate_monthly_installment()
        self.due_dates = self.calculate_due_dates()

    def calculate_monthly_installment(self):
        monthly_rate = self.interest_rate / 100 / 12
        emi = (self.total_amount * monthly_rate * (1 + monthly_rate) ** self.tenure_months) / ((1 + monthly_rate) ** self.tenure_months - 1)
        return round(emi, 2)
    
    def calculate_due_dates(self) -> List[datetime]:
        due_dates = [datetime.now() + timedelta(days=30 * i) for i in range(1, self.tenure_months + 1)]
        return due_dates

    def calculate_penalty(self, months: int):
        return self.late_fee * months

    def get_plan_details(self):
        return {
            "user_id": self.user_id,
            "purchase_id": self.purchase_id,
            "total_amount": self.total_amount,
            "remaining_balance": self.remaining_balance,
            "interest_rate": self.interest_rate,
            "tenure_months": self.tenure_months,
            "monthly_installment": self.monthly_installment,
        }