


# To see the details of the products present in database





import mysql.connector

def ProductDisplay() :

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()

    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from product_details;")
    product_Database = mycursor.fetchall()

    product_Details = []

    for i in product_Database :
        product_Details.append(list(i))

    productLength_max_list = []

    print("\n\t\t\t\t\t\t\t\t\tProduct At Shopping Cart")

    if len(product_Details) == 0 :
        print("\nNo Products Present In Shopping Cart")

    else : 
        print("\n")
        for j in range(len(product_Details)) : 
            productLength_max_list.append(len(product_Details[j][1]))

        productLength_max = max(productLength_max_list)

        print("\tProduct Name\t\t\t\t\tPrice (In ₹)\t\t\t Brand Name")

        for i in range(len(product_Details)) : 
        
            if productLength_max >= len(product_Details[i][1]) : 
                equaliser_factor = productLength_max - len(product_Details[i][1])
                equaliser_space = equaliser_factor * " "

                print("\n",i+1,".\t",product_Details[i][1] + equaliser_space,"\t\t\t\t",product_Details[i][2],"\t\t\t\t",product_Details[i][3])
                print(" ")


def ProductDisplay_Admin() :

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()

    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from product_details;")
    product_Database = mycursor.fetchall()

    product_Details = []

    for i in product_Database :
        product_Details.append(list(i))

    productLength_max_list = []

    print("\n\t\t\t\t\t\t\t\t\tProduct At Shopping Cart")

    if len(product_Details) == 0 :
        print("\nNo Products Present In Shopping Cart")

    else : 
        print("\n")
        for j in range(len(product_Details)) : 
            productLength_max_list.append(len(product_Details[j][1]))

        productLength_max = max(productLength_max_list)

        print("Product_Id\t\tProduct Name\t\t\t\tPrice (In ₹)\t\t\t Brand Name\t\t\tAccount_Creation_Info")

        for i in range(len(product_Details)) : 
        
            if productLength_max >= len(product_Details[i][1]) : 
                equaliser_factor = productLength_max - len(product_Details[i][1])
                equaliser_space = equaliser_factor * " "

                print("\n",product_Details[i][0],"\t\t\t",product_Details[i][1] + equaliser_space,"\t\t\t",product_Details[i][2],"\t\t\t\t",product_Details[i][3],"\t\t\t",product_Details[i][4])
                print(" ")