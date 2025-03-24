import mysql.connector



# Asking permission to add product from same category
try:
    def choice_to_add_from_same_category(table_name,category_name,cart,quantity):
        from product_category import category_list
        from DB_product import show_product
        new_product=input(f"\nDo you want to add more products from same category? (Y/N): ").upper()
        if new_product == "Y":
            show_product(table_name,category_name,category_list)
        elif new_product=="N":
            print("\nThank you for visiting.")
            new_product=choice_to_add_from_different_category(table_name,cart,quantity)
        
        return table_name,category_name,cart

    def choice_to_add_from_different_category(table_name,cart,quantity):
        from product_category import select_category
        from Cart_Amount import Total
        new_product=input("\nDo you want to add product from different category? (Y/N): ").upper()
        if new_product == "Y":
            select_category(table_name)
        elif new_product=="N":
            print("\nThank you for shopping.\n")           
            Total(cart,table_name,quantity)

        return new_product
    
except mysql.connector.Error as err:
    print(f"Error: {err}")