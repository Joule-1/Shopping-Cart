

# Customer Log In


import mysql.connector
import Gmail_Module
import otpValidate_Module

def login() : 

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()
    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from customer_details;")
    customer_database = mycursor.fetchall()

    customer_details = []
    customer_name = []

    for i in customer_database :
        customer_details.append(i)

    for j in range(len(customer_details)) :
        customer_name.append(customer_details[j][0])

 
    print("\n\t\t\t\t\t\t\t\t\t\tLogin To Shopping Cart")
    name = input("\nEnter Customer\'s Name : ")
    phone = input("\nEnter Customer\'s Phone Number : ")

    name = name.strip()
    phone = phone.strip()
    
    for k in range(len(customer_details)) : 
 
        if phone == customer_details[k][1] :
 
            if name == customer_details[k][0] and name.isalpha() == True and name != "User Name"  : 

                customer_mail = customer_details[k][2]

                otp = Gmail_Module.sendMail(customer_mail)

                return otpValidate_Module.otp(otp) 

            else : 
                print("\n\tUser Information Is Not Correct")
                return False       
    else :
        print("\n\tCustomer Is Not Registered Or Incorrect Name With Shopping Cart")
        return False
