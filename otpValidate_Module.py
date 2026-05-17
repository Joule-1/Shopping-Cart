

# Check One Time Password (OTP) Entered By The User

def otp(otp_gen) : 
   
    otp_gen = str(otp_gen)
    
    for i in range(3): 
        i = i + 1

        otp_user = input("\n\tEnter The One Time Password(OTP) Sent To Your Gmail Inbox : ")
        otp_user = otp_user.strip()

        if str(otp_gen) == otp_user : 
            print("\nYou Have Successfully Logged In To Shopping Cart")   
            return True 
        else  :
            print("\nOne Time Password(OTP) Entered Is Incorrect")
    else :
        print("\n\tOne Time Password(OTP) Entered Is Incorrect")
        print("\nTime Out")
        return False
