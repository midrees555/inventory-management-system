# inventory_operations.py

# Initial empty set to store items in inventory
inventory = set()


# function to add an item
def add_item(catalog):
    item = input("Enter item to add: ").title()

    if item not in inventory:
        inventory.add(item)
        catalog.add(item)                                       # adding the item to catalog if not already there
        print(f"\n{item} added to inventory successfully!")
    else:
        print(f"{item} is already in the inventory.")
    
    print("---------------------------------------")


# function to remove an item
def remove_item(catalog):
    item = input("Enter item to remove: ").title()
    if item in inventory:
        inventory.remove(item)
        print(f"{item} removed from inventory successfully!")
        
    else:
        print(f"{item} not found in the inventory.")

    print("--------------------------------")


# function to check if an item is in stock? (is item in stock, return bool)
def is_in_stock(item):
    return item in inventory

# Function to list all available items in invetory
def list_available_items():
    print("Available Items in inventory :")
    print("-----------------------------")
    if inventory:
        pass
        for item in inventory:
            print(f"--> {item}")
    else:
        print("Inventory is empty.")

    print("-----------------------------")


# Function to exit the system
def exit_system():
    print("Exiting the system...")
    print("-------------------------------------------------------------------\n")
    exit()