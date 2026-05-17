
# First Page


import DatabaseCheck
DatabaseCheck.databasechecker()  
import Customer_Details_Module
import Customer_Removal_Module
import Emp_Details_Module
import Emp_Removal_Module
import Emp_SignUp_Module
import Emp_Login_Module
import Product_Add_Module
import Product_Display_Module
import Product_PriceUpdate_Module
import Product_Removal_Module


def end() : 
    print(" ") 
    print("*"*177)
    print(" ")


def FirstDisplay() :

    print("\n\n\t\t\t\t\t\t\t\t\t          Welcome To Shopping Cart")

    while True :  
                 
        print("""

    \t\t\t\t\t\t\t\t\t\t       Employee Login

    \t\t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * *
    \t\t\t\t\t\t\t\t\t*                                           *                                  
    \t\t\t\t\t\t\t\t\t*\ta. Login                            *  
    \t\t\t\t\t\t\t\t\t*                                           * 
    \t\t\t\t\t\t\t\t\t*\tb. Admin                            *
    \t\t\t\t\t\t\t\t\t*                                           * 
    \t\t\t\t\t\t\t\t\t*\tc. Exit                             *
    \t\t\t\t\t\t\t\t\t*                                           * 
    \t\t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * *                                                    
                                                                    """)

        firstChoice = input("\n\tEnter Your Choice(a-c) : ")
        firstChoice = firstChoice.strip()
        firstChoice = firstChoice.lower()

        if firstChoice == "a" :  
            Emp_Login_Module.login()
            FirstDisplay()
            exit()

        elif firstChoice == "b" :
            admin_function()
            exit()

        elif firstChoice == "c" :
            end()
            exit()

        else :
            print("\n\tEnter Your Choice Between The Given Serial Number")



#                                   Admin

 

def admin_function() : 

    admin = input("\nEnter Admin Password : ")
    admin = admin.strip()
    admin = admin.lower()

    if admin == "123" : 
   
        while True :           
            
            print("""
    
            \t\t\t\t\t\t\t\t\t  Admin Functions

            \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * *
            \t\t\t\t\t\t\t\t*                                           *                                  
            \t\t\t\t\t\t\t\t*\ta. About Customer                   *  
            \t\t\t\t\t\t\t\t*                                           *                                                          
            \t\t\t\t\t\t\t\t*\tb. About Employee                   *
            \t\t\t\t\t\t\t\t*                                           *
            \t\t\t\t\t\t\t\t*\tc. About Product                    *
            \t\t\t\t\t\t\t\t*                                           *
            \t\t\t\t\t\t\t\t*\td. Return To Previous Display       *
            \t\t\t\t\t\t\t\t*                                           * 
            \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * 
                                                                                """)
            admin_choice = input("\n\tEnter Your Choice(a-d) : ")
            admin_choice = admin_choice.strip()
            admin_choice = admin_choice.lower()

            if admin_choice == "a" :
                customer_About() 
                exit()

            elif admin_choice == "b" : 
                employee_About()
                exit()
            
            elif admin_choice == "c" : 
                Product_About()
                exit()

            elif admin_choice == "d" : 
                FirstDisplay()
                exit()

            else : 
                print("\n\tEnter Your Choice Between The Given Serial Number")  
    else : 
        print("\n\tIncorrect Password")
        FirstDisplay()


def customer_About() : 

    while True : 

        print("""
 
        \t\t\t\t\t\t\t\t\t  About Customer

        \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * *
        \t\t\t\t\t\t\t\t*                                           *                                  
        \t\t\t\t\t\t\t\t*\ta. Customer Details                 *  
        \t\t\t\t\t\t\t\t*                                           *                                                          
        \t\t\t\t\t\t\t\t*\tb. Remove Customer                  *
        \t\t\t\t\t\t\t\t*                                           *                                                          
        \t\t\t\t\t\t\t\t*\tc. Return To Previous Display       *
        \t\t\t\t\t\t\t\t*                                           * 
        \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * 
                                                                            """)

        customer = input("\n\tEnter Your Choice(a-c) : ")
        customer = customer.strip()
        customer = customer.lower()

        if customer == "a" :
            Customer_Details_Module.customer_details()
            customer_About()
            exit()

        elif customer == "b" : 
            Customer_Details_Module.customer_details()
            Customer_Removal_Module.Customer_Remove()
            customer_About()
            exit()

        elif customer == "c" :
            admin_function()
            exit()

        else : 
            print("\n\tEnter Your Choice Between The Given Serial Number")


def employee_About() : 

     while True : 

        print("""
 
        \t\t\t\t\t\t\t\t\t  About Employee

        \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * *
        \t\t\t\t\t\t\t\t*                                           *                                  
        \t\t\t\t\t\t\t\t*\ta. Employee Details                 *  
        \t\t\t\t\t\t\t\t*                                           *                                                          
        \t\t\t\t\t\t\t\t*\tb. Remove Employee                  *
        \t\t\t\t\t\t\t\t*                                           * 
        \t\t\t\t\t\t\t\t*\tc. Employee Sign Up                 *
        \t\t\t\t\t\t\t\t*                                           * 
        \t\t\t\t\t\t\t\t*\td. Employee Login                   *
        \t\t\t\t\t\t\t\t*                                           *                                                          
        \t\t\t\t\t\t\t\t*\te. Return To Previous Display       *
        \t\t\t\t\t\t\t\t*                                           * 
        \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * 
                                                                            """)

        employee = input("\n\tEnter Your Choice(a-e) : ")
        employee = employee.strip()
        employee = employee.lower()

        if employee == "a" :
            Emp_Details_Module.employee_details()
            employee_About()
            exit()

        elif employee == "b" : 
            Emp_Details_Module.employee_details()
            Emp_Removal_Module.Emp_Remove()
            employee_About()
            exit()

        elif employee == "c" : 
            Emp_SignUp_Module.sign()
            employee_About()
            exit()
        
        elif employee == "d" : 
            Emp_Login_Module.login()
            FirstDisplay()
            exit()

        elif employee == "e" :
            admin_function()
            exit()

        else : 
            print("\n\tEnter Your Choice Between The Given Serial Number")


def Product_About() : 

     while True : 

        print("""
 
        \t\t\t\t\t\t\t\t\t  About Product

        \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * *
        \t\t\t\t\t\t\t\t*                                           *                                  
        \t\t\t\t\t\t\t\t*\ta. Product Details                  *  
        \t\t\t\t\t\t\t\t*                                           *                                                          
        \t\t\t\t\t\t\t\t*\tb. Add Product                      *
        \t\t\t\t\t\t\t\t*                                           *
        \t\t\t\t\t\t\t\t*\tc. Update Product Price             *
        \t\t\t\t\t\t\t\t*                                           *                                
        \t\t\t\t\t\t\t\t*\td. Remove Product                   *  
        \t\t\t\t\t\t\t\t*                                           *                                                          
        \t\t\t\t\t\t\t\t*\te. Return To Previous Display       *
        \t\t\t\t\t\t\t\t*                                           * 
        \t\t\t\t\t\t\t\t* * * * * * * * * * * * * * * * * * * * * * * 
                                                                            """)

        employee = input("\n\tEnter Your Choice(a-e) : ")
        employee = employee.strip()
        employee = employee.lower()

        if employee == "a" :
            Product_Display_Module.ProductDisplay_Admin()
            Product_About()
            exit()
 
        elif employee == "b" : 
            Product_Display_Module.ProductDisplay_Admin()
            Product_Add_Module.product_Addition()
            Product_About()
            exit()
 
        elif employee == "c" : 
            Product_Display_Module.ProductDisplay_Admin()
            Product_PriceUpdate_Module.Update_Product_Price()
            Product_About()
            exit()
 
        elif employee == "d" : 
            Product_Display_Module.ProductDisplay_Admin()
            Product_Removal_Module.Remove_Product() 
            Product_About()
            exit()

        elif employee == "e" :
            admin_function()
            exit()
        else : 
            print("\n\tEnter Your Choice Between The Given Serial Number")

         
FirstDisplay()