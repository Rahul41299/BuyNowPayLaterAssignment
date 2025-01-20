from models.user import User

class UserService:
    def __init__(self):
        self.users = {}
    
    def register_user(self, user_id: str, name: str, credit_limit: float):
        if user_id in self.users:
            return {"status": "Error", "message": "User already exists"}
        user = User(user_id, name, credit_limit)
        self.users[user_id] = user
        return {"status": "Success", "message": "User registered successfully"}
    
    def get_user(self, user_id: str):
        if user_id not in self.users:
            return {"status": "Error", "message": "User not found"}
        return self.users[user_id].get_user_details()
    
    def get_available_credit(self, user_id: str):
        user = self.get_user(user_id)
        if not user:
            return {"status": "Error", "message": "User not found"}
        return {"status": "Success", "available_credit": user.get_available_credit()}