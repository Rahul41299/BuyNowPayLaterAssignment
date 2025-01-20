from models.payment import Payment
from services.user_service import UserService
from services.repayment_service import RepaymentService

class PaymentService:
    def __init__(self, user_service: UserService, repayment_service: RepaymentService):
        self.user_service = user_service
        self.repayment_service = repayment_service
        self.payments = {}

    def make_payment(self, payment_id: str, user_id: str, purchase_id: str, amount: float):
        user = self.user_service.get_user(user_id)
        if not user:
            return {"status": "Error", "message": "User not found"}

        payment = Payment(payment_id, user_id, amount)
        self.payments[payment_id] = payment

        repayment_result = self.repayment_service.process_payment(user_id, purchase_id, amount)

        return {"status": "Success", "message": "Payment recorded", "details": repayment_result}

    def get_payment_history(self, user_id: str):
        payments = [p.get_payment_details() for p in self.payments.values() if p.user_id == user_id]
        return {"status": "Success", "payment_history": payments}
