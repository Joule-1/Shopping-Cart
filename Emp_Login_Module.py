

# Employee Login



import mysql.connector
import Gmail_Module
import Product_Receipt_Generator_Module
import otpValidate_Module





def login() : 
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()
    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from employee_details;")
    emp_database = mycursor.fetchall()

    emp_details = []
    emp_name = []

    for i in emp_database :
        emp_details.append(i) 

    for j in range(len(emp_details)) :
        emp_name.append(emp_details[j][0])

    print("\n\t\t\t\t\t\t\t\t\t\tLogin To Shopping Cart")
    name = input("\nEnter Your Name : ")
    password = input("\nEnter Your Password : ")
    phone = input("\nEnter Your Registered Mobile Number : ")

    name = name.strip()
    password = password.strip()
    phone = phone.strip()

    for k in range(len(emp_details)) : 
 
        if phone == emp_details[k][2] :    

            if password == emp_details[k][1] and name == emp_details[k][0] and name != "User Name"  :                

                emp_mail = emp_details[k][4]

                otp = Gmail_Module.sendMail(emp_mail)
 
                check = otpValidate_Module.otp(otp)

                if check == True : 
                    Product_Receipt_Generator_Module.bill()
                    break

                else : 
                    pass
                    break
            else : 
                print("\n\tEmployee Information Incorrect")           
                break      
    else :
        print("\n\tMobile Number Is Not Registered With Shopping Cart")
