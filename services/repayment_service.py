from models.repayment import EMIPlan, RepaymentPlan
from services.user_service import UserService

class RepaymentService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.repayment_plans = {}

    def add_repayment_plan(self, purchase_id: str, plan: RepaymentPlan):
        self.repayment_plans[purchase_id] = plan

    def process_payment(self, user_id: str, purchase_id: str, amount: float):
        user = self.user_service.get_user(user_id)
        if not user:
            return {"status": "Error", "message": "User not found"}

        plan = self.repayment_plans.get(purchase_id)
        if not plan:
            return {"status": "Error", "message": "Repayment plan not found"}

        plan.update_payment(amount)
        user.update_credit(amount)

        return {"status": "Success", "message": f"Payment of {amount} applied to {purchase_id}"}

    def calculate_penalty(self, purchase_id: str, missed_months: int):
        plan = self.repayment_plans.get(purchase_id)
        if not plan or not isinstance(plan, EMIPlan):
            return {"status": "Error", "message": "No EMI plan found"}

        penalty = plan.calculate_penalty(missed_months)
        return {"status": "Success", "penalty_amount": penalty}
