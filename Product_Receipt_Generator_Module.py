

# Generate Bill For Customer

import Product_Display_Module
import random
import Customer_SignUp_Module
import Customer_Login_Module
import mysql.connector
 
mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
mycursor = mydb.cursor()

mycursor.execute("use shopping_cart;")
mycursor.execute("select * from product_details;")
product_Database = mycursor.fetchall()

product_Detailss = []

for i in product_Database :
    product_Detailss.append(list(i))

RandomfreeProduct = 0
RandomfreeProductPrice = 0
RandomfreeProductGetPrice = 0

RandomfreeProductNumber = random.randrange(len(product_Detailss))
RandomfreeProduct = product_Detailss[RandomfreeProductNumber][1]
RandomfreeProductPrice = product_Detailss[RandomfreeProductNumber][2]
RandomfreeProductGetPrice = random.randint(6000,10000)


bill_Data = {}


def bill() : 
    
    print("\n\tToday's Special Offer, For Shopping More Than ₹",RandomfreeProductGetPrice,"You Will Get A Free",RandomfreeProduct,"Of Worth ₹",RandomfreeProductPrice)

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()

    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from product_details;")
    product_Database = mycursor.fetchall()

    product_Details = []

    for i in product_Database :
        product_Details.append(list(i))
    
    
    bill_Data["Product"] = ["Price Per Unit(In ₹)","Quantity","Amount(In ₹)"]

    Product_Display_Module.ProductDisplay()

    product_Choice = input("\nEnter The Serial Number Of The Product Required : ")
    product_Choice = product_Choice.strip()

    if product_Choice.isdigit() == True and int(product_Choice) <= len(product_Details) : 

        product_Choice = int(product_Choice)
        product_Name = product_Details[product_Choice - 1][1]

        if product_Choice >= 1 and product_Choice <= len(product_Details) : 
            print("\n\tYou Have Selected ",product_Name,"Of Price : ₹",product_Details[product_Choice - 1][2])

            product_Quantity = input("\nEnter The Quantity Of "+product_Name+" Required : ")
            product_Quantity = product_Quantity.strip()
            productQuantityDigitCheck = product_Quantity.isdigit()

            if productQuantityDigitCheck == True : 

                product_Quantity = int(product_Quantity)

                if product_Quantity >= 1 and product_Quantity <= 99 :
                    
                    if product_Name in bill_Data and int(bill_Data[product_Name][1]) + product_Quantity <= 99  :  

                        bill_Data[product_Name] = [product_Details[product_Choice - 1][2] , str(product_Quantity + int(bill_Data[product_Name][1])) , str(int(product_Details[product_Choice - 1][2]) * (product_Quantity + int(bill_Data[product_Name][1])) ) ]

                    elif product_Name not in bill_Data and product_Quantity <= 99 : 

                        bill_Data[product_Name] = [product_Details[product_Choice - 1][2] , str(product_Quantity) , str(int(product_Details[product_Choice - 1][2]) * product_Quantity) ]
                    else :
                        if product_Name in bill_Data and int(bill_Data[product_Name][1]) + product_Quantity >= 100  :
                            print("\nProduct Buying Limit Reached Of 99 Units \n\n\tYou Cannot Buy More Units Of",product_Name,"On A Single Bill")
                        else : 
                            print("\n\tThis Is A Retail Shop, You Can Not Purchase The Quantity Of",product_Name,"Greater Than 99 Units")
                else : 
                    print("\n\tThis Is A Retail Shop, You Can Not Purchase The Quantity Of",product_Name,"Greater Than 99 Units")
            else :
                print("\n\tEnter Correct Quantity Of Product")
        else : 
            print("\n\tEnter Correct Serial Number Of Product")     
    else : 
        print("\n\tEnter Correct Serial Number Of Product") 

    MoreProduct()

def MoreProduct() :
    
    while True :
    
        print(""" 

        \t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        \t\t\t\t\t\t\t*                                                               *            
        \t\t\t\t\t\t\t*\ta. Do You Want To Continue To Buy Other Products        * 
        \t\t\t\t\t\t\t*                                                               *  
        \t\t\t\t\t\t\t*\tb. Bill Payment                                         *
        \t\t\t\t\t\t\t*                                                               *  
        \t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
                                                                                            """)                                                                               
        exitChoice = input("Enter Your Choice (a-b) : ")
        exitChoice = exitChoice.strip()
        exitChoice = exitChoice.lower()

        if exitChoice == "a" : 
            bill()
            break

        elif exitChoice == "b" : 
            receipt()
            break

        else : 
            print("\n\tEnter Your Choice Between The Given Serial Number")

def receipt() : 
    
    ProductName_bill_Data = list(bill_Data.keys())
    ProductPrice_bill_Data = list(bill_Data.values())

    ProductLength_maxList = []
    PriceLength_maxList = []
    QuantityLength_maxList = []

    for j in range(len(ProductName_bill_Data)) : 

        ProductLength_maxList.append(len(ProductName_bill_Data[j]))                       # Product Alignment
        PriceLength_maxList.append(len(ProductPrice_bill_Data[j][0]))                        # Price Alignment
        QuantityLength_maxList.append(len(ProductPrice_bill_Data[j][1]))                     # Quantity Alignment

    PriceLength_max = max(PriceLength_maxList)                                   # Price Alignmet
    ProductLength_max = max(ProductLength_maxList)                               # Product Alignment
    QuantityLength_max = max(QuantityLength_maxList)                             # Quantity Alignment

    print("\n\t\t\t\t\t\t\t\t\t\tBill")

    for i in range(len(ProductName_bill_Data)) :

        if ProductLength_max > len(ProductName_bill_Data[i]) :                     # Product Alignmet
            diff1 = ProductLength_max - len(ProductName_bill_Data[i])
            ProductName_bill_Data[i] = ProductName_bill_Data[i] + " " * diff1

        if PriceLength_max > len(ProductPrice_bill_Data[i][0]) :                      # Price Alignment
            diff2 = PriceLength_max - len(ProductPrice_bill_Data[i][0])
            ProductPrice_bill_Data[i][0] = ProductPrice_bill_Data[i][0] + " " * diff2

        if QuantityLength_max > len(ProductPrice_bill_Data[i][1]) :                   # Quantity Alignment
            diff3 = QuantityLength_max - len(ProductPrice_bill_Data[i][1])
            ProductPrice_bill_Data[i][1] = ProductPrice_bill_Data[i][1] + " " * diff3

        if i == 0 : 
            a = " "
        else : 
            a = i 

        print("\n",a,"\t",ProductName_bill_Data[i],"\t\t\t\t",ProductPrice_bill_Data[i][0],"\t\t\t\t",ProductPrice_bill_Data[i][1],"\t\t\t",ProductPrice_bill_Data[i][2])
        print(" ")
    billProduct_Modify()

def billProduct_Modify() :
    
    while True : 

        print(""" 

        \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * *
        \t\t\t\t\t\t\t\t*                                                   *                                  
        \t\t\t\t\t\t\t\t*\ta. Increase Quantity Of Any Product         *  
        \t\t\t\t\t\t\t\t*                                                   * 
        \t\t\t\t\t\t\t\t*\tb. Decrease Quantity Of Any Product         *
        \t\t\t\t\t\t\t\t*                                                   *
        \t\t\t\t\t\t\t\t*\tc. Add Product                              *
        \t\t\t\t\t\t\t\t*                                                   *
        \t\t\t\t\t\t\t\t*\td. Remove Any Product                       *
        \t\t\t\t\t\t\t\t*                                                   * 
        \t\t\t\t\t\t\t\t*\te. Final Bill                               *       
        \t\t\t\t\t\t\t\t*                                                   * 
        \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * * 
        
                                                                            """)

        Change_Choice = input("Enter Your Choice(a-e) : ")
        Change_Choice = Change_Choice.strip()
        Change_Choice = Change_Choice.lower()

        if Change_Choice == "a" : 
            ProductQuantity_Increase()
            break   

        elif Change_Choice == "b" : 
            ProductQuantity_Decrease()
            break

        elif Change_Choice == "c" : 
            bill()
            break

        elif Change_Choice == "d" : 
            Product_Remove()
            break

        elif Change_Choice == "e" : 
            FinalBill()
            break

        else : 
            print("\n\tEnter Your Choice Between The Given Serial Number")


def ProductQuantity_Increase() : 
 
    ProductName_bill_Data = list(bill_Data.keys())
    ProductPrice_bill_Data = list(bill_Data.values())

    product_Choice = input("\nEnter The Serial Number Of Product Your Want To Increase The Quantity : ")
    product_Choice = product_Choice.strip()

    if product_Choice.isdigit() == True :
        
        product_Choice = int(product_Choice)

        if product_Choice <= len(ProductName_bill_Data) - 1 and product_Choice > 0 : 

            print("\n\tYou Have Selected",ProductName_bill_Data[product_Choice],": ₹",ProductPrice_bill_Data[product_Choice][0])
            print("\nCurrent Quantity Of",ProductName_bill_Data[product_Choice],"in Bill :",ProductPrice_bill_Data[product_Choice][1])

            quantity_Increase = input("\nEnter The Number Of Unit To Be Increased Of "+ProductName_bill_Data[product_Choice]+" : ")
            quantity_Increase = quantity_Increase.strip()

            if quantity_Increase.isdigit() == True :

                quantity_Increase = int(quantity_Increase)

                if quantity_Increase <= 99 and int(ProductPrice_bill_Data[product_Choice][1]) <= 99 and quantity_Increase + int(ProductPrice_bill_Data[product_Choice][1]) <= 99: 

                    ProductPrice_bill_Data[product_Choice][1] = int(ProductPrice_bill_Data[product_Choice][1]) + quantity_Increase
                    ProductPrice_bill_Data[product_Choice][2] = ProductPrice_bill_Data[product_Choice][1] * int(ProductPrice_bill_Data[product_Choice][0])
                    ProductPrice_bill_Data[product_Choice][2] = str(ProductPrice_bill_Data[product_Choice][2])                                      # Amount In Bill
                    ProductPrice_bill_Data[product_Choice][1] = str(ProductPrice_bill_Data[product_Choice][1])                                      # Quantity In Bill                            

                    print("\n\tNew Quantity Of",ProductName_bill_Data[product_Choice],"Present In The Bill : ",ProductPrice_bill_Data[product_Choice][1])
                else : 
                    print("\n\tTotal Quantity Of" , ProductName_bill_Data[product_Choice] ,"Can Not Be Greater Than 99")
            else : 
                print("\n\tEnter Correct Quantity Of The Product")
        else : 
            print("\n\tEnter Correct Serial Number")
    else :
        print("\n\tEnter Correct Serial Number")
            
    receipt()


def ProductQuantity_Decrease() : 

    ProductName_bill_Data = list(bill_Data.keys())
    ProductPrice_bill_Data = list(bill_Data.values())
  
    product_Choice = input("\nEnter The Serial Number Of Product Your Want To Decrease The Quantity : ")
    product_Choice = product_Choice.strip()

    if product_Choice.isdigit() == True :
        
        product_Choice = int(product_Choice)
 
        if product_Choice <= len(ProductName_bill_Data) - 1 and product_Choice > 0  : 

            print("\n\tYou Have Selected",ProductName_bill_Data[product_Choice],": ₹",ProductPrice_bill_Data[product_Choice][0])
            print("\nCurrent Quantity Of",ProductName_bill_Data[product_Choice],"in Bill :",ProductPrice_bill_Data[product_Choice][1])

            quantity_Decrease = input("\nEnter The Number Of Unit To Be Decrease Of "+ProductName_bill_Data[product_Choice]+" : ")
            quantity_Decrease = quantity_Decrease.strip()
            quantityDigitCheck = quantity_Decrease.isdigit()

            if quantityDigitCheck == True :

                quantity_Decrease = int(quantity_Decrease)

                if int(quantity_Decrease) >= 1 and int(ProductPrice_bill_Data[product_Choice][1]) <= 99 :

                    if int(quantity_Decrease) > int(ProductPrice_bill_Data[product_Choice][1]) : 
                        print("\n\tQuantity To Be Decreased Can Not Be Greater Than The Quantity Present In The Bill")
                    else : 

                        ProductPrice_bill_Data[product_Choice][1] = int(ProductPrice_bill_Data[product_Choice][1]) - int(quantity_Decrease)
                        ProductPrice_bill_Data[product_Choice][2] = ProductPrice_bill_Data[product_Choice][1] * int(ProductPrice_bill_Data[product_Choice][0])
                        ProductPrice_bill_Data[product_Choice][2] = str(ProductPrice_bill_Data[product_Choice][2])                                      # Amount In Bill
                        ProductPrice_bill_Data[product_Choice][1] = str(ProductPrice_bill_Data[product_Choice][1])

                    print("\n\tNew Quantity Of",ProductName_bill_Data[product_Choice],"Present In The Bill : ",ProductPrice_bill_Data[product_Choice][1])
                else : 
                    print("\n\tTotal Quantity Of" , ProductName_bill_Data[product_Choice] ,"Can Not Be Greater Than 99 Or Less Than 0")
            else : 
                print("\n\tEnter Correct Quantity Of The Product")
        else : 
            print("\n\tEnter Correct Serial Number")
    else : 
        print("Enter The Correct Serial Number")
        
    receipt()


def Product_Remove() : 

    ProductName_bill_Data = list(bill_Data.keys())
    ProductPrice_bill_Data = list(bill_Data.values())

    if len(ProductName_bill_Data) == 1 : 
        print("\n\tYour Cart Is Empty")
        print("\nYou Can Not Remove Any Product")
        billProduct_Modify()

    else : 

        product_Choice = input("\nEnter The Serial Number Of The Product To Be Removed : ")
        product_Choice = product_Choice.strip()

        if product_Choice.isdigit() == True : 

            product_Choice = int(product_Choice)

            if product_Choice <= len(ProductName_bill_Data) - 1 and product_Choice > 0 : 

                print("\n\tYou Have Selected",ProductName_bill_Data[product_Choice],": ₹",ProductPrice_bill_Data[product_Choice][0])

                bill_Data.pop(ProductName_bill_Data[product_Choice])

                print("\n\t",ProductName_bill_Data[product_Choice],"Is Removed Successfully From Your Bill")

            else : 
                print("\n\tEnter Correct Serial Number")
        else : 
            print("\n\tEnter The Correct Serial Number")

        receipt()

def FinalBill() : 

    ProductName_bill_Data = list(bill_Data.keys())
    ProductPrice_bill_Data = list(bill_Data.values())

    ProductLength_maxList = []
    PriceLength_maxList = []

    for j in range(len(ProductName_bill_Data)) : 

        ProductLength_maxList.append(len(ProductName_bill_Data[j]))  
        PriceLength_maxList.append(len(ProductPrice_bill_Data[j][0]))                        # Price Alignment
    PriceLength_max = max(PriceLength_maxList)                                               # Product Alignmet
    ProductLength_max = max(ProductLength_maxList)

    print("\n\t\t\t\t\t\t\t\t\t\tBill")

    for i in range(len(ProductName_bill_Data)) :

        if ProductLength_max > len(ProductName_bill_Data[i]) :                     # Product Alignmet
            diff1 = ProductLength_max - len(ProductName_bill_Data[i])
            ProductName_bill_Data[i] = ProductName_bill_Data[i] + " " * diff1

        if PriceLength_max > len(ProductPrice_bill_Data[i][0]) :                      # Price Alignment
            diff2 = PriceLength_max - len(ProductPrice_bill_Data[i][0])
            ProductPrice_bill_Data[i][0] = ProductPrice_bill_Data[i][0] + " " * diff2

        if i > 0 : 
            ProductPrice_bill_Data[i][2] = "\t " + ProductPrice_bill_Data[i][2]

        print("\n\t",ProductName_bill_Data[i],"\t\t\t\t",ProductPrice_bill_Data[i][0],"\t\t\t\t",ProductPrice_bill_Data[i][1],"\t\t\t",ProductPrice_bill_Data[i][2])
        print(" ")
           
    amount = []
    for l in range(len(ProductPrice_bill_Data)) : 

        if l == 0 : 
            continue

        else : 
            amount.append(int(ProductPrice_bill_Data[l][2]))

    global TotalAmount
    TotalAmount = sum(amount)

    print("\tAmount To Be Paid : ₹",TotalAmount)

    for m in range(len(ProductName_bill_Data)) : 
        ProductName_bill_Data[m] = ProductName_bill_Data[m].strip()
        if m == 0 : 
            continue
        else : 
            del bill_Data[ProductName_bill_Data[m]]
 
    Payment_Option()


def Payment_Option() :     

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="0000")
    mycursor = mydb.cursor()

    mycursor.execute("use shopping_cart;")
    mycursor.execute("select * from product_details;")
    product_Database = mycursor.fetchall()

    product_Details = []

    for i in product_Database :
        product_Details.append(list(i))

    while True : 

        print(""" 

    \t\t\t\t\t\t\t\t\t\tPay Via

    \t\t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   
    \t\t\t\t\t\t\t\t\t*                                                             *                                  
    \t\t\t\t\t\t\t\t\t*\ta. Customer Login, For Discount And Free Products     *  
    \t\t\t\t\t\t\t\t\t*                                                             *     
    \t\t\t\t\t\t\t\t\t*\tb. Without Login                                      *
    \t\t\t\t\t\t\t\t\t*                                                             *  
    \t\t\t\t\t\t\t\t\t*\tc. Customer Sign Up, For Discount And Free Products   * 
    \t\t\t\t\t\t\t\t\t*                                                             *         
    \t\t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   
                                                                                 """)
        Payment_Choice = input("Enter Your Choice(a-b) : ")
        Payment_Choice = Payment_Choice.strip()
        Payment_Choice = Payment_Choice.lower()

        if Payment_Choice == "a" : 

            work = Customer_Login_Module.login()

            if work == True :

                discount = random.randint(5,13)
 
                if TotalAmount >= 200 :

                    print("\n\tCongratulations, You Have Been Given A Discount Of",discount,"%")
                    discountAmount = (TotalAmount * discount)/100

                    finalAmount = TotalAmount - discountAmount

                    print("\n\nAmount To Be Paid After Discount : ₹",finalAmount) 

                else :
                    print("\n\tAmount To Be Paid : ₹",TotalAmount)

                if TotalAmount >= RandomfreeProductGetPrice : 

                    print("\nYou Will Get A Free",RandomfreeProduct,"Of Worth ₹",RandomfreeProductPrice,"For Shopping More Than ₹",RandomfreeProductGetPrice)
               
            else :
                print("\n\tLogin Failed\nEnter Your Correct Information")
                Payment_Option()
                 
            break     

        elif Payment_Choice == "b" : 
            print("\n\tAmount To Be Paid : ₹",TotalAmount)
            break

        elif Payment_Choice == "c" : 
            
            if Customer_SignUp_Module.sign() == True :
    
                discount = random.randint(5,13)
 
                if TotalAmount >= 500 :

                    print("\n\tCongratulations, You Have Been Given A Discount Of",discount,"%")
                    discountAmount = (TotalAmount * discount)/100

                    finalAmount = TotalAmount - discountAmount

                    print("\n\nAmount To Be Paid After Discount : ₹",finalAmount) 

                else : 
                    print("\n\tAmount To Be Paid : ₹",TotalAmount)

                if TotalAmount >= RandomfreeProductGetPrice : 
                    print("\nYou Will Get A Free",RandomfreeProduct,"Of Worth ₹",RandomfreeProductPrice,"For Shopping More Than ₹",RandomfreeProductGetPrice)
            else :
                print("\n\tSign Up Failed\n\nEnter Your Correct Information")
                Payment_Option()
                
            break
        else : 
            print("\n\tEnter Your Choice Between The Given Serial Number")
    print("\n\t\tThanks For Shopping")
 
    while True : 
        print(""" 

            \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * *
            \t\t\t\t\t\t\t\t*                                                   *                                  
            \t\t\t\t\t\t\t\t*\ta. Next Customer                            *  
            \t\t\t\t\t\t\t\t*                                                   * 
            \t\t\t\t\t\t\t\t*\tb. Return To Main Menu                      *       
            \t\t\t\t\t\t\t\t*                                                   * 
            \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * * 
                                                                                   """)
        emp_choice = input("Enter Your Choice(a-b) : ")
        emp_choice = emp_choice.strip()
        emp_choice = emp_choice.lower()

        if emp_choice == "a" : 
            bill()
            break
        elif emp_choice == "b" : 
            pass
            break 
        else :             
            print("\n\tEnter Your Choice Between The Given Serial Number")
