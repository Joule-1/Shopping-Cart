def validator(name, password, email, role):
    if not nameValidate(name):
        return False, "Name is invalid. It should be at least 2 characters long and contain only alphabets."
    
    if not passwordValidate(password):
        return False, "Password is invalid. It should be at least 8 characters long and contain at least one digit, one uppercase letter, and one lowercase letter."
    
    if not emailValidate(email):
        return False, "Email entered is invalid."
    
    if not roleValidate(role):
        return False, "Role entered is invalid. It should be either 'employee' or 'customer'."
    return True

def nameValidate(name):
    if len(name) < 2:
        return False
    if not name.strip().isalpha():
        return False
    return True

def passwordValidate(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

def emailValidate(email, otp):
    if "@" not in email or "." not in email:
        return False
    systemGeneratedOtp = otpGenerator()
    if otp != systemGeneratedOtp:
        return False
    return True

def roleValidate(role):
    valid_roles = ["employee", "customer"]
    if role.lower() not in valid_roles:
        return False
    return True