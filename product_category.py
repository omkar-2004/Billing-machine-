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

    # Show category.
    try:
        category_list=[]
        def show_category(table_name,mycursor):
            mycursor.execute(f"select distinct(category) from {table_name};")
            category_list.clear()
            for x in mycursor:
                category_list.append(x[0])
            print("\nCategory available in mart.")
            for i in category_list:
                print(f"\t{i}")
            return table_name
        
        def select_category(table_name):  
            import DB_product  
            show_category(table_name,mycursor)
            category_name=input("\nEnter the category of item you want to search from above : ").upper()
            DB_product.show_product(table_name,category_name,category_list)
            return table_name
               
    except mysql.connector.Error as err:
        print(f"Error: {err}")

except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f"Something went wrong: {err}")
