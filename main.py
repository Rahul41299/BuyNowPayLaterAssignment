from models.user import User
from models.payment import Payment
from models.repayment import FixedPaymentPlan, EMIPlan
from models.purchase import Purchase

if __name__ == "__main__":
    user1 = User("user1", "Alice", 1000)
    user2 = User("user2", "Bob", 2000)
    purchase1 = Purchase("purchase1", user1.user_id, 500)
    purchase2 = Purchase("purchase2", user2, 1500)
    emi_plan = EMIPlan(purchase1.user_id, purchase1.purchase_id, purchase1.amount, 5, 100, 10)
    fixed_plan = FixedPaymentPlan(purchase2.user_id, purchase2.purchase_id, purchase2.amount)
    payment1 = Payment(user1, emi_plan, 100)
    payment2 = Payment(user2, fixed_plan, 500)

    emi_plan.update_payment(100)
    emi_plan.update_payment(200)

    print(emi_plan.get_plan_details())
    print(user1.get_available_credit())
