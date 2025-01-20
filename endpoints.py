from services.user_service import UserService
from services.purchase_service import PurchaseService
from services.repayment_service import RepaymentService
from services.payment_service import PaymentService


user_service = UserService()
repayment_service = RepaymentService(user_service)
purchase_service = PurchaseService(user_service)
payment_service = PaymentService(user_service, repayment_service)


class RegisterUserRequest():
    user_id: str
    name: str
    credit_limit: float


class PurchaseRequest():
    user_id: str
    purchase_id: str
    amount: float
    emi_plan: dict = None


class PaymentRequest():
    payment_id: str
    user_id: str
    purchase_id: str
    amount: float


#Endpoints

# post("/users/")
def register_user(request: RegisterUserRequest):
    return user_service.register_user(request.user_id, request.name, request.credit_limit)


# get("/users/{user_id}/credit")
def get_available_credit(user_id: str):
    return user_service.get_available_credit(user_id)


# post("/purchases/")
def make_purchase(request: PurchaseRequest):
    return purchase_service.make_purchase(request.user_id, request.purchase_id, request.amount, request.emi_plan)


# get("/purchases/{purchase_id}")
def get_purchase_details(purchase_id: str):
    return purchase_service.get_purchase(purchase_id)


# post("/payments/")
def make_payment(request: PaymentRequest):
    return payment_service.make_payment(request.payment_id, request.user_id, request.purchase_id, request.amount)


# get("/users/{user_id}/payments")
def get_payment_history(user_id: str):
    return payment_service.get_payment_history(user_id)


# get("/purchases/{purchase_id}/penalty")
def calculate_penalty(purchase_id: str, missed_months: int):
    return repayment_service.calculate_penalty(purchase_id, missed_months)
