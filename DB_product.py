import mysql.connector



# database connection
try:
    # passcode=input("Enter the password:")
    mydb = mysql.connector.connect(
        host="127.0.0.1",  # Or 127.0.0.1
        user="root",      # Your MySQL username
        password='Omkar@2004',  # Your MySQL password
        database='mart' 
    )
    # print("\nConnection successful!\n")
    
    
    # Now you can interact with the database
    mycursor = mydb.cursor()
    
    try:
        product_list=[]  
        price_list=[]      
        def show_product(table_name,category_name,category_list):
            import product_category
            if category_name in category_list:
                mycursor.execute(f"SELECT product_name FROM {table_name} where category= '{category_name}';")
                product_list.clear()
                for x in mycursor:
                    product_list.append(x[0])        
                mycursor.execute(f"SELECT price FROM {table_name} where category= '{category_name}';")
                price_list.clear()
                for x in mycursor:
                    price_list.append(x[0]) 
                product_price_list=dict(zip(product_list,price_list))
                for x in product_price_list:
                    print(f"{x} Rs.{product_price_list[x]}")
                select_product(table_name,category_name,product_price_list)      
            else:
                print("\nCategory is not in mart")
                product_category.select_category(table_name)
            return table_name,category_name
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    # to select product to cart
    try:
        cart=[]
        pn=[]
        ql=[]
        def select_product(table_name,category_name,product_price_list):
            product="Y"
            import choice
            while product=="Y":
                product_name=input(f"\nEnter the product name to add to cart=").upper()
                quan=input("Enter the quntity of the product you want to add in the cart:")
                if product_name not in pn:
                    pn.append(product_name)
                    ql.append(quan)
                if product_name in product_list:
                    mycursor.execute(f"SELECT product_name FROM {table_name} where category= '{category_name}' and Product_name='{product_name}';")
                    if product_name not in cart: 
                        for product_name in mycursor:
                            cart.append(product_name[0])
                        quantity=dict(zip(pn,ql))
                        print(f"\n{quan} X {product_name[0]} of Rs.{product_price_list[product_name[0]]} is added in cart")  
                        
                    else:
                        print(f"\n{product_name} is already in cart.try again")
                else:
                    print("\nProduct not available or check the spelling.")
                new_product=choice.choice_to_add_from_same_category(table_name,category_name,cart,quantity)
                product=new_product
            return table_name,category_name
    
    except Exception as err:
        print(f"Error: {err}")
except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f"Something went wrong: {err}")
