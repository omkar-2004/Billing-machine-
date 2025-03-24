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
        # To show tables in database.
        try:
            table_list=[]
            def show_table():
                mycursor.execute("SHOW TABLES;")
                table_list.clear()
                for x in mycursor:
                    table_list.append(x[0])
                print(f"\nTables in mart database:-")
                for i in table_list: 
                    print(f"\t{i}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        # To select data.
        try:
            def select_data():
                import product_category
                # show_table()
                # table_name=input("\nEnter the table name to select from above:")
                table_name='product'
                product_category.select_category(table_name)
                # if table_name in table_list:
                #     print(f"\n{table_name} table is selected.\n")
                #     product_category.select_category(table_name)
                # else:
                #     print(f"\n{table_name} table is not in  mart database.\n")
                #     select_data()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    except Exception as e:
        print(e)
        
    try:
        select_data()
    except Exception as e:
        print(f"Error:{e}")
    
except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f"Something went wrong: {err}")
        
finally:
    # Close the connection (important for releasing resources)
    if mydb.is_connected():
        mycursor.close()
        mydb.close()