

# Employee Sign Up



import datetime
import mysql.connector
import Gmail_Module
import Emp_ValidateDOB_Module
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
    mycursor.execute("select * from employee_details;")
    emp_database = mycursor.fetchall()

    emp_details = []

    for i in emp_database :
        emp_details.append(i)

      

    print("\n\t\t\t\t\t\t\t\t\t\tSign To Shopping Cart")
    name = input("\nEnter Your Name : ")
    name = name.strip()
    name = name.lower()

    password = input("\nCreate Your Password : ")
    password = password.strip()

    if len(name) <= 3 or len(name) >= 101 or len(password) <= 3 or len(password) >= 101 : 
        print("\n\tName Or Password Cannot Contain Characters Less Than 4 Or Greater Than 100")

    elif name == password : 
        print("\n\tName And Password Can Not Be Same")
    
    elif name.isidentifier() == False or name.isdigit() == True : 
        print("\n\tName Can Only Contain Alphabets")

    else : 

        dob = Emp_ValidateDOB_Module.dob_approval() 

        if dob != False : 

            phone = input("\nEnter Your Mobile Number : +91 ")
            phone = phone.strip()
            phone_digitCheck = phone.isdigit()

            if phone != password : 

                for i in range(len(emp_details)) : 

                    if phone in emp_details[i][2] : 
                        print("\n\tMobile Number Is Already Registered With Shopping Cart")
                        break
                    
                    elif " " in phone : 
                        print("\n\tEnter Correct Phone Number")
                        break

                else :

                    if phone_digitCheck == True and len(phone) == 10 and phone != "0000000000"  : 


                        email = input("\nEnter Your Gmail Id : ")
                        email = email.strip()

                        for x in range(len(emp_details)) : 
                            if email == emp_details[x][4] :
                                print("\n\tGmail Already Registered")
                                break
                        else :
    
                            if email != emp_details[x][4] : 

                                if email[-10:] == "@gmail.com" :

                                    otp = Gmail_Module.sendMail(email)

                                    check = otpValidate_Module.otp(otp)


                                    if check == True : 

                                        account = str(datetime.datetime.today())[:16]
                                        
                                        mycursor.execute("insert into employee_details values (%s, %s, %s, %s, %s, %s)",(name,password,phone,dob,email,account))
                                    
                                        mydb.commit()
                                        mycursor.close()
                                        
                                        print("\nCongratulations,",name,"You Have Been Registered To Shopping Cart")
                                    
                                    else : 
                                        pass
                                else : 
                                    print("\n\tEnter Your Correct Gmail Id")
                            else : 
                                print("\n\tEnter Your Correct Gmail Id")  
                    else : 
                        print("\n\tEnter Your Correct Phone Number")
            else : 
                print("\n\tMobile Number And Password Can Not Be Same")
        else : 
            print("\nEnter Your Correct Date Of Birth")    
