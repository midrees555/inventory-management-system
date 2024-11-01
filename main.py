# Real Project: Inventory Management System
# Design a system where:

# Each unique item type is stored in a set.
# Users can add or remove items from the set.
# Perform operations like checking if an item is in stock, finding out-of-stock items, or listing all available items.
#----------------------------------------->
# Solution :

from inventory_operations import add_item, remove_item, is_in_stock, list_available_items, exit_system
from inventory_analysis import find_out_of_stock, inventory_summary

catalog = {"laptop", "Mouse", "Keyboard", "Airpods", "Desk", "Chair"}

def inventory_operation_choices():
    """Prints choices for inventory operations for the user to perform"""

    print("\nWhat do you want yo perform?")
    print("------------------------------")
    print("1. To Add an item")
    print("2. To Remove an item")
    print("3. Check if an item is 'In Stock'")
    print("4. Check if an item is 'Out Of Stock'")
    print("5. View 'inventory Summary'")
    print("6. Exit The System")
    print("------------------------------------")
    

def main():
    """Main function to run the inventory management system."""

    print("\n|---------------------------------------|")
    print(" Welcom To 'inventory Management System'!")
    print("|---------------------------------------|")
    
    while True:
        inventory_operation_choices()
        choice = input("Select an options: ").strip()

        if choice == '1':
            add_item(catalog)
        
        elif choice == '2':
            remove_item(catalog)
        
        elif choice == '3':
            item = input("Enter item to check: ")

            if is_in_stock(item):
                print(f"Yes! {item} is in stock!")
            else:
                print(f"Sorry! {item} is out of stock.")
            
        elif choice == '4':
            out_of_stock_items = find_out_of_stock(catalog)
            if out_of_stock_items:
                print("--------------------")
                print("Out of stock items: ")

                for item in out_of_stock_items:
                    print(f"--> {item}")
            else:
                print("All catalog items are in stock.")
                
            print("-------------------------------")
        
        elif choice == '5':
            summary = inventory_summary()
            print("-------------------")
            print(f"Total items : {inventory_summary()["total_items"]}")

            for item in summary["in_stock_items"]:
                print(f"--> {item}")
            print("----------------")

        elif choice == '6':
            exit_system()

        else:
            print("Invlide choice! Please try again.")
            print("---------------------------------")

if __name__ == "__main__":
    main()