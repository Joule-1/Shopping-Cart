
# Remove Customer Account From The Database 


import mysql.connector

def Customer_Remove() :

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()
    mycursor.execute("use shopping_cart;")

    customer_details = []
 
    mycursor.execute("select * from customer_details;")
    customer_database = mycursor.fetchall()

    for j in customer_database :
        customer_details.append(list(j)) 
    
    phone = input("\nEnter Phone Number Of User You Want To Remove : ")
    phone = phone.strip()
 
    if len(customer_details) != 0 :

        if len(customer_details) != 1 : 

            for i in range(len(customer_details)) :
             
                if phone == customer_details[i][1] : 
                    mycursor.execute("delete from customer_details where Phone_Number = {}".format(customer_details[i][1]))
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
