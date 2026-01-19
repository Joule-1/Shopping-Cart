import random

def otpGenerator():
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return otp  
