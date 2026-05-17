

# Customer Sign Up


import datetime
import mysql.connector
import Gmail_Module
import otpValidate_Module

 
wayYes = "yes" , "y"
wayNo = "no" , "n"
 
def end() :
    print(" ") 
    print("*"*177)
    print(" ")

def sign() :

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()

    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from customer_details;")
    customer_database = mycursor.fetchall()

    customer_details = []

    for i in customer_database :
        customer_details.append(i)

      

    print("\n\t\t\t\t\t\t\t\t\t\tSign To Shopping Cart")
    name = input("\nEnter Customer\'s Name : ")
    name = name.strip()
    name = name.lower()


    if len(name) <= 3 or len(name) >= 101 : 
        print("\n\tName Cannot Contain Characters Less Than 4 Or Greater Than 100")

    elif name.isidentifier() == False or name.isdigit() == True : 
        print("\n\tName Can Only Contain Alphabets")

    else :          
        phone = input("\nEnter Customer\'s Mobile Number : +91 ")
        phone = phone.strip()
        phone_digitCheck = phone.isdigit()

        for i in range(len(customer_details)) : 

            if phone in customer_details[i][1] : 
                print("\n\tMobile Number Is Already Registered With Shopping Cart")
                break
            
            elif " " in phone : 
                print("\n\tEnter Correct Phone Number")
                break

        else :

            if phone_digitCheck == True and len(phone) == 10 and phone != "0000000000"  : 


                email = input("\nEnter Customer\'s Gmail Id : ")
                email = email.strip()

                for x in range(len(customer_details)) : 
                    if email == customer_details[x][2] :
                        print("\n\tGmail Already Registered")
                        return False
                else :

                    if email != customer_details[x][2] : 

                        if email[-10:] == "@gmail.com" :

                            otp = Gmail_Module.sendMail(email)

                            check = otpValidate_Module.otp(otp)

                            if check == True : 

                                account = str(datetime.datetime.today())[:16]
                                
                                mycursor.execute("insert into customer_details values (%s, %s, %s, %s)",(name,phone,email,account))
                            
                                mydb.commit()
                                mycursor.close()
                                
                                print("\nCongratulations,",name,"You Have Been Registered To Shopping Cart")

                                return True
                                exit()
                            
                            else : 
                                return False
                                pass                            
                        else : 
                            print("\n\tEnter Your Correct Gmail Id")
                            return False
                    else : 
                        print("\n\tEnter Your Correct Gmail Id")  
                        return False
            else : 
                print("\n\tEnter Your Correct Phone Number")
                return False
