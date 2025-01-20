from datetime import datetime
from typing import Optional

from models.repayment import RepaymentPlan

class Purchase:
    def __init__(self, purchase_id: str, user_id: str, amount: float, repayment_plan: Optional[RepaymentPlan] = None):
        self.purchase_id = purchase_id
        self.user_id = user_id
        self.amount = amount
        self.timestamp = datetime.now()
        self.repayment_plan = repayment_plan

    def get_purchase_details(self) -> dict:
        return {
            "purchase_id": self.purchase_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "repayment_plan": self.repayment_plan.get_plan_details() if self.repayment_plan else "Full Payment"
        }