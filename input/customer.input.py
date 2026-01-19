def customer_input():
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    customer_email = input("Enter Customer Email: ")
    customer_address = input("Enter Customer Address: ")
    customer_phone = input("Enter Customer Phone: ")
    
    return customer_id, customer_name, customer_email, customer_address, customer_phone

customer_input()