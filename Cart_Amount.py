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
    
    def Total(cart,table_name,quantity):
        price=[]
        cost=0
        for l in range(0,len(cart)):
            mycursor.execute(f"SELECT price FROM {table_name} WHERE Product_name='{cart[l]}';")
            for x in mycursor:
                price.append(x[0])
                
        cart_price=dict(zip(cart,price))
        print("Product\t\t\t|Quantity\t|unit_price\t|Total price|")
        for t in cart_price:
            cost=cost+(cart_price[t]*int(quantity[t]))
            print(f"{t}\t\t\t|{quantity[t]}\t\t|Rs.{cart_price[t]}\t\t|Rs.{(cart_price[t]*int(quantity[t]))}|")
        print(f"Total Amount:{cost}")
        cost=0
        f=open("bill.txt","w")
        f.write("Product\t\t\t|Quantity\t|unit_price\t|Total price|\n")
        for t in cart_price:
            cost=cost+(cart_price[t]*int(quantity[t]))
            f.write(f"{t}\t\t\t|{quantity[t]}\t\t|Rs.{cart_price[t]}\t\t|Rs.{(cart_price[t]*int(quantity[t]))}|\n")
        f.write(f"Total Amount:{cost}")
            
            
            
    
        
except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f"Something went wrong: {err}")
        
