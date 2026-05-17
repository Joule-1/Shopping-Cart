
# Update Price of Product

import mysql.connector
 
def Update_Product_Price() : 

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()

    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from product_details;")
    product_database = mycursor.fetchall()

    product_details = []

    for i in product_database :
        product_details.append(list(i))
 
    
    product_id = input("Enter Product_Id : ")
    product_id = product_id.strip()
    product_id = product_id.upper()

    for i in range(len(product_details)) : 

        if product_details[i][0] == product_id : 
 
                
            price = input("\nEnter The Updated Price Of "+product_details[i][1]+" : ₹ ")
            price = price.strip()
            
            if price.isdigit() == True and len(price) <= 4 : 

                mycursor.execute("update product_details set price = (%s) where product_id = (%s)",(price,product_details[i][0]))
                mydb.commit()
                mycursor.close()
                print("\n\tPrice Of",product_details[i][1],"Updated Successfully")
                break

            else : 
                print("\n\tEnter Correct Price Of Product\tPrice Of Product Can Not Be Greater Than 9999")
                break
    else : 
        print("\n\tProduct Does Not Exist In Shopping Cart")
