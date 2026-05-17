
# Create database and tables

import mysql.connector

import pickle

 
def databasechecker() : 
    try : 
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")

        database_create = "create database shopping_cart"
        database_use = "use shopping_cart"
        employee_details = "create table Employee_Details (Employee_Name varchar(200) not null, Password varchar(50) not null, Phone_Number char(10) not null primary key, Date_Of_Birth char(10) not null, Email_Id varchar(700) not null unique, Account_Creation_Info char(16) not null);"
        product_details = "create table Product_Details (Product_Id varchar(3) not null primary key, Product_Name varchar(400) not null, Price varchar(5) not null, Brand_Name varchar(700) not null, Account_Creation_Info char(16) not null);"
        customer_details = "create table Customer_Details (Customer_Name varchar(200) not null, Phone_Number char(10) not null primary key, Email_Id varchar(700) not null unique, Account_Creation_Info char(16) not null);"
    
        mycursor = mydb.cursor()

        mycursor.execute(database_create)
        mycursor.execute(database_use)
        mycursor.execute(employee_details)
        mycursor.execute(product_details)
        mycursor.execute(customer_details)
        
            
        data1 = open("cus.dat","rb")
        a = pickle.load(data1)
        data1.close()

        for i in range(len(a)) : 
            mycursor.execute("insert into customer_details values(%s, %s, %s, %s)",(a[i][0],a[i][1],a[i][2],a[i][3]))
            mydb.commit()
        
        
        data2 = open("emp.dat","rb")
        b = pickle.load(data2)
        data2.close()

        for j in range(len(b)) : 
            mycursor.execute("insert into employee_details values(%s, %s, %s, %s, %s, %s)",(b[j][0],b[j][1],b[j][2],b[j][3],b[j][4],b[j][5]))
            mydb.commit()

        data3 = open("pro.dat","rb")
        c = pickle.load(data3)
        data3.close()
    
        for k in range(len(c)) :
            mycursor.execute("insert into product_details values(%s, %s, %s, %s, %s)",(c[k][0],c[k][1],c[k][2],c[k][3],c[k][4]))
            mydb.commit()
    except : 
        pass
