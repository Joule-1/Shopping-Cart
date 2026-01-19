class User:
    def __init__(self, user_id, user_name, user_password, user_email, user_address, user_phone, user_role):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_role = user_role
    
    def getUserID(self, id):
        return self.user_id
    
    def getUserName(self, name):
        return self.user_name
    
    def getUserPassword(self, password):
        return self.user_password
    
    def getUserEmail(self, email):
        return self.user_email  
    
    def getUserRole(self, role):
        return self.user_role
    
    def setUserName(self, name):
        self.user_name = name
    
    def setUserPassword(self, password):
        self.user_password = password

    def setUserEmail(self, email):
        self.user_email = email

class Employee(User):
    def __init__(self, user_id, user_name, user_password, user_email, user_role):
        super().__init__(user_id, user_name, user_password, user_email, user_role)

class Customer(User):
    def __init__(self, user_id, user_name, user_password, user_email, user_role):
        super().__init__(user_id, user_name, user_password, user_email, user_role)