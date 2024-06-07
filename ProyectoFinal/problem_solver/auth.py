import bcrypt
class Auth:
    @staticmethod
    def generate_hash(password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hashed_password.decode()
    
    @staticmethod
    def compare_password(hashed_password, password):
       
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
    
