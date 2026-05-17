

# Remove Employee Details From Database



import mysql.connector

def Emp_Remove() : 

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()
    mycursor.execute("use shopping_cart;")

    emp_details = []
    emp_name = []

    mycursor.execute("select * from employee_details;")
    emp_database = mycursor.fetchall()

    for j in emp_database :
        emp_details.append(list(j))
    
    phone = input("\nEnter The Phone Number Of Employee You Want To Remove : ")
    phone = phone.strip()
    phone = phone.lower()

    if len(emp_details) != 0 :

        if len(emp_details) != 1 :

            for i in range(len(emp_details)) :
            
                if phone == emp_details[i][2] : 
                    mycursor.execute("delete from employee_details where Phone_Number = {}".format(emp_details[i][2]))
                    mydb.commit()
                    mycursor.close()
                    print("\n\tAccount Deleted Successfully")     
                    break  
                            
            else : 
                print("\n\tNo User Exist With This Phone Number Does Not Exist")
                print("")
                 
        else : 
            print("\n\tYou Can Not Remove User, When Only 1 User Is Registered") 
    else : 
        print("\n\tUnder Maintenance\n\tSorry For Inconvenience")
