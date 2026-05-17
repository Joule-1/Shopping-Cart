
# Add New Product To Database

import mysql.connector
import datetime


def product_Addition() : 

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()
 
    mycursor.execute("use shopping_cart;")

    Product_details = []
 
    mycursor.execute("select * from product_details;")
    Product_database = mycursor.fetchall()

    for j in Product_database :
        Product_details.append(list(j))

    print("\n\t\t\t\t\t\t\t\t\t\tAdd Product To Shopping Cart")

    print("""
    
    Add Products In The Following Format : 
    
        Bread (1 Packet)    Rice (1 Kg)     Cooking Oil (1 Litre)

        Note : Price Should Be For A Single Product Only
        
                                                                    """)

    add_Product = input("Enter Product To Be Added To Shopping Cart : ")
    add_Product = add_Product.strip()
    add_Product = add_Product.title()

    add_Brand = input("\n\tEnter The Name Of Company Selling The Product : ")
    add_Brand = add_Brand.strip()
    add_Brand = add_Brand.title()

    for i in range(len(Product_details)) : 

        if add_Product == Product_details[i][1] :

            if add_Brand == Product_details[i][3] : 

                print("\n\tProduct Is Already Registered With Shopping Cart")
                break   

    else : 
        add_Brand = add_Brand + " "
        add_Product = add_Product + " "
        if add_Product.isspace() == False and add_Brand.isspace() == False and "(" in add_Product and ")" in add_Product :
            add_Brand = add_Brand.strip()
            add_Product = add_Product.strip()

            position = add_Product.index("(")

            if "1" in add_Product and add_Product[-1] == ")" and add_Product[position + 1] == "1" and add_Product[position + 2] == " " and add_Product[position - 1] == " "   :

                add_Price = input("\nEnter The Price Of "+add_Product+" ₹ : ")
                add_Price = add_Price.strip()

                if add_Price.isdigit() == True and len(add_Price) <= 4 :  

                    addition_product = str(datetime.datetime.today())[:16]         

                    product_id = int(Product_details[-1][0][2:]) + 1
                    product_id = "P_" + str(product_id)

                    mycursor.execute("insert into product_details values (%s, %s, %s, %s, %s)",(product_id,add_Product,add_Price,add_Brand,addition_product))
                    mydb.commit()
                    mycursor.close()

                    print("\n\tProduct Added Successfully To Shopping Cart")

                else :                       
                    print("\n\tEnter Correct Price Of Product\tPrice Of Product Can Not Be Greater Than 9999")
            else : 
                print("\n\tEnter The Product Name In Given Format")
        else :
            print("\n\tEnter The Product Name In Given Format")
