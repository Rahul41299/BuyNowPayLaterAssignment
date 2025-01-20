from models.purchase import Purchase
from models.repayment import FixedPaymentPlan, EMIPlan
from services.user_service import UserService

class PurchaseService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.purchases = {}

    def make_purchase(self, user_id: str, purchase_id: str, amount: float, emi_plan=None):
        user = self.user_service.get_user(user_id)
        if not user:
            return {"status": "Error", "message": "User not found"}

        if user.available_credit < amount:
            return {"status": "Error", "message": "Insufficient credit"}

        if emi_plan:
            plan = EMIPlan(user_id, purchase_id, amount, emi_plan['interest_rate'], emi_plan['tenure_months'], emi_plan['late_fee'])
        else:
            plan = FixedPaymentPlan(user_id, purchase_id, amount)

        purchase = Purchase(purchase_id, user_id, amount, plan)
        self.purchases[purchase_id] = purchase
        user.update_credit(-amount)

        return {"status": "Success", "message": f"Purchase of {amount} recorded", "purchase_id": purchase_id}

    def get_purchase(self, purchase_id: str):
        purchase = self.purchases.get(purchase_id)
        if not purchase:
            return {"status": "Error", "message": "Purchase not found"}
        return purchase.get_purchase_details()
