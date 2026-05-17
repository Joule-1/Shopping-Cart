

# To See Details Of Customer Stored In Database 



import mysql.connector

def customer_details() :

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()

    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from customer_details;")
    customer_database = mycursor.fetchall()

    customer_details = []
    customer_name = []

    for x in customer_database :
        customer_details.append(list(x))

    for j in range(len(customer_details)) :
        customer_name.append(customer_details[j][0])
 
   
    print("\n\t\t\t\t\t\t\t\t\t\tCustomer Details")

    if len(customer_details) == 0 :
        print("\n 0 Customer Are Registered To Shopping Cart")

    else : 
        print(" ")

        customer_name[0] = customer_name[0] + " " * 11                                                # User Name Alignment
        customer_details[0][1] = customer_details[0][1] + " " * 12                                          # Password Alignment
        
        print("\n Name \t\t\t Phone Number \t\t\t Gmail Id \t\t\t\t Account Creation Info")
        for i in range(len(customer_name)) :

            if len(customer_name[0]) > len(customer_name[i])  :                                       # User Name Alignment
                diff1 = len(customer_name[0]) - len(customer_name[i])
                customer_name[i] = customer_name[i] + diff1 * " "

            if len(customer_details[0][1]) > len(customer_details[i][1])  :                                 # Password Alignment
                diff2 = len(customer_details[0][1]) - len(customer_details[i][1])
                customer_details[i][1] = customer_details[i][1] + diff2 * " "

            customer_details[i][1] = str(customer_details[i][1])                                            # Date Of Birth Alignment

            if len(customer_details[0][1]) > len(customer_details[i][1])  :                                 # Date Of Birth Alignment
                diff3 = len(customer_details[0][1]) - len(customer_details[i][1])
                customer_details[i][1] = customer_details[i][1] + diff3 * " "    

            if len(customer_details[0][2]) > len(customer_details[i][2])  :                                 # Phone Number Alignment
                diff4 = len(customer_details[0][2]) - len(customer_details[i][2])
                customer_details[i][2] = customer_details[i][2] + diff4 * " "

        
            print("\n",customer_name[i],"\t",customer_details[i][1],"\t",customer_details[i][2],"\t\t",customer_details[i][3])
            i = i + 1

            print(" ")
        print("\n",i,"Customer Are Registered To Shopping Cart")
