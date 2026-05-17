

# Remove Product From Database


import mysql.connector

  

def Remove_Product() : 

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()        


    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from product_details;")
    product_database = mycursor.fetchall()

    product_details = []

    for i in product_database :
        product_details.append(list(i))

    if len(product_details) != 1 :
 
        product_id = input("Enter Product_Id : ")
        product_id = product_id.strip()
        product_id = product_id.upper()

        for i in range(len(product_details)) : 

            if product_details[i][0] == product_id : 

                deleted = product_details[i][0]
                deleted = "'{}'".format(product_details[i][0])
                mycursor.execute("delete from product_details where product_id = {};".format(deleted))
                mydb.commit()
                mycursor.close()
                print("\n\t",product_details[i][1],"Product Removed Successfully")
                break  
        else : 
            print("\n\tProduct Does Not Exist In Shopping Cart") 
    else : 
        print("\n\tYou Can Not Remove Products When There Is Only 1 Product Left In Inventory")
