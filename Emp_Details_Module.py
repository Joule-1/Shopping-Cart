

# To see Employee Details Stored In Database

import mysql.connector



def employee_details() :

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()

    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from employee_details;")
    emp_database = mycursor.fetchall()

    emp_details = []
    emp_name = []

    for x in emp_database :
        emp_details.append(list(x))

    for j in range(len(emp_details)) :
        emp_name.append(emp_details[j][0])
 
   
    print("\n\t\t\t\t\t\t\t\t\t\tEmployee Details")

    if len(emp_details) == 0 :
        print("\n 0 Employee Are Woking At Shopping Cart")
         
    else : 
        print(" ")

        emp_name[0] = emp_name[0] + " " * 11                                                # User Name Alignment
        emp_details[0][1] = emp_details[0][1] + " " * 12                                          # Password Alignment
        
        print("\n Name \t\t\t Password \t\t Phone Number \t\t Date Of Birth \t\t Gmail Id \t\t\t\t Account Creation Info")
        for i in range(len(emp_name)) :

            if len(emp_name[0]) > len(emp_name[i])  :                                       # User Name Alignment
                diff1 = len(emp_name[0]) - len(emp_name[i])
                emp_name[i] = emp_name[i] + diff1 * " "

            if len(emp_details[0][1]) > len(emp_details[i][1])  :                                 # Password Alignment
                diff2 = len(emp_details[0][1]) - len(emp_details[i][1])
                emp_details[i][1] = emp_details[i][1] + diff2 * " "

            emp_details[i][1] = str(emp_details[i][1])                                            # Date Of Birth Alignment

            if len(emp_details[0][1]) > len(emp_details[i][1])  :                                 # Date Of Birth Alignment
                diff3 = len(emp_details[0][1]) - len(emp_details[i][1])
                emp_details[i][1] = emp_details[i][1] + diff3 * " "    

            if len(emp_details[0][2]) > len(emp_details[i][2])  :                                 # Phone Number Alignment
                diff4 = len(emp_details[0][2]) - len(emp_details[i][2])
                emp_details[i][2] = emp_details[i][2] + diff4 * " "

            emp_details[i][3] = str(emp_details[i][3])                                            # Account Creation Date Alignment

            if len(emp_details[0][3]) > len(emp_details[i][3])  :                                 # Account Creation Date Alignment
                diff5 = len(emp_details[0][3]) - len(emp_details[i][3])
                emp_details[i][3] = emp_details[i][3] + diff5 * " "  

            if len(emp_details[0][4]) > len(emp_details[i][4])  :                                 # Account Creation Alignment
                diff6 = len(emp_details[0][4]) - len(emp_details[i][4])
                emp_details[i][4] = emp_details[i][4] + diff6 * " "
        
            print("\n",emp_name[i],"\t",emp_details[i][1],"\t",emp_details[i][2],"\t\t",emp_details[i][3],"\t\t",emp_details[i][4],"\t\t",emp_details[i][5])
            i = i + 1
 
            print(" ")
        print("\n",i,"Employee Are Working At Shopping Cart")
