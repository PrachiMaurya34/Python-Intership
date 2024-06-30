                         # assignment 5
# Assignment: Inventory Management System for a Grocery Store with File and Exception Handling
import datetime
class Product:
    def __init__(self, name, category, price, quantity, expiration_date):
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
    def is_expired(self):
        return self.expiration_date < datetime.datetime.now()
class Inventory:
    def __init__(self):
        self.products = []
        self.categorized_products = {}
    def add_product(self, name, category, price, quantity, expiration_date):
        try:
            product = Product(name, category, price, quantity, expiration_date)
            self.products.append(product)
            self.categorize_products()
            print(f"Product '{name}' added to the inventory.")
        except Exception as e:
            print(f"Error adding product: {e}")
    def remove_product(self, name):
        product_to_remove = None
        for product in self.products:
            if product.name == name:
                product_to_remove = product
                break
        if product_to_remove:
            self.products.remove(product_to_remove)
            self.categorize_products()
            print(f"Product '{name}' removed from the inventory.")
        else:
            print(f"Product '{name}' not found in the inventory.")
    def search_products(self, search_term):
        results = [product for product in self.products if search_term.lower() in product.name.lower() or search_term.lower() in product.category.lower()]
        if results:
            print("Search results:")
            for product in results:
                print(f"Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}, Expiration Date: {product.expiration_date.strftime('%Y-%m-%d')}")
        else:
            print("No products matching the search term found.")
    def list_products(self):
        if self.products:
            print("Products in the inventory:")
            for product in self.products:
                print(f"Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}, Expiration Date: {product.expiration_date.strftime('%Y-%m-%d')}")
        else:
            print("The inventory is empty.")
    def categorize_products(self):
        self.categorized_products = {}
        for product in self.products:
            category = product.category
            if category not in self.categorized_products:
                self.categorized_products[category] = []
            self.categorized_products[category].append(product)
        for category, products in self.categorized_products.items():
            print(f"Category: {category}")
            for product in products:
                print(f"  Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}, Expiration Date: {product.expiration_date.strftime('%Y-%m-%d')}")
    def check_and_remove_expired_products(self):
        self.products = [product for product in self.products if not product.is_expired()]
        self.categorize_products()
        print("Expired products removed from the inventory.")
    def save_inventory_to_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                for product in self.products:
                    file.write(f"{product.name},{product.category},{product.price},{product.quantity},{product.expiration_date.strftime('%Y-%m-%d')}\n")
            print("Inventory saved successfully.")
        except Exception as e:
            print(f"Error saving inventory: {e}")
    def load_inventory_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    name, category, price, quantity, expiration_date = line.strip().split(',')
                    product = Product(name, category, price, quantity, expiration_date)
                    self.products.append(product)
            self.categorize_products()
            print("Inventory loaded successfully.")
        except Exception as e:
            print(f"Error loading inventory: {e}")
def main():
    inventory = Inventory()
    while True:
        print("\nInventory Menu:")
        print("1. Add a product")
        print("2. Remove a product")
        print("3. Search for a product")
        print("4. List all products")
        print("5. Categorize products")
        print("6. Check for expired products")
        print("7. Save inventory to file")
        print("8. Load inventory from file")
        print("9. Exit")
        choice = input("Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): ")
        if choice == 'Add':
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = input("Enter product price: ")
            quantity = input("Enter product quantity: ")
            expiration_date = input("Enter product expiration date (YYYY-MM-DD): ")
            inventory.add_product(name, category, price, quantity, expiration_date)
        elif choice == 'Remove':
            name = input("Enter name of product to remove: ")
            inventory.remove_product(name)
        elif choice == 'Search':
            search_term = input("Enter product name or category to search: ")
            inventory.search_products(search_term)
        elif choice == 'List':
            inventory.list_products()
        elif choice == 'Categorize':
            inventory.categorize_products()
        elif choice == 'Check':
            inventory.check_and_remove_expired_products()
        elif choice == '':
            inventory.save_inventory_to_file('inventory.txt')
        elif choice == '8':
            inventory.load_inventory_from_file('inventory.txt')
        elif choice == '9':
            print("Exiting the inventory system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
# PS C:\Users\piyu\OneDrive\Desktop\python> & "C:/Program Files/Python312/python.exe" c:/Users/piyu/OneDrive/Desktop/python/Assignment5.py/Assignment5.py

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Add
# Enter product name: Watch
# Enter product category: Devices
# Enter product price: 20000
# Enter product quantity: 1
# Enter product expiration date (YYYY-MM-DD): 2027-04-04
# Category: Devices
#   Name: Watch, Price: 20000.0, Quantity: 1, Expiration Date: 2027-04-04
# Product 'Watch' added to the inventory.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Save
# Enter file path to save inventory: inventory.txt
# Inventory saved successfully.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Add 
# Enter product name: Apple 
# Enter product category: Fruits
# Enter product price: 120
# Enter product quantity: 1
# Enter product expiration date (YYYY-MM-DD): 2025-01-01
# Category: Devices
#   Name: Watch, Price: 20000.0, Quantity: 1, Expiration Date: 2027-04-04
# Category: Fruits
#   Name: Apple, Price: 120.0, Quantity: 1, Expiration Date: 2025-01-01
# Product 'Apple' added to the inventory.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Add
# Enter product name: Mango
# Enter product category: Fruits
# Enter product price: 150
# Enter product quantity: 2
# Enter product expiration date (YYYY-MM-DD): 2023-01-04
# Category: Devices
#   Name: Watch, Price: 20000.0, Quantity: 1, Expiration Date: 2027-04-04
# Category: Fruits
#   Name: Apple, Price: 120.0, Quantity: 1, Expiration Date: 2025-01-01
#   Name: Mango, Price: 150.0, Quantity: 2, Expiration Date: 2023-01-04
# Product 'Mango' added to the inventory.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): List
# Products in the inventory:
# Name: Watch, Category: Devices, Price: 20000.0, Quantity: 1, Expiration Date: 2027-04-04
# Name: Apple, Category: Fruits, Price: 120.0, Quantity: 1, Expiration Date: 2025-01-01   
# Name: Mango, Category: Fruits, Price: 150.0, Quantity: 2, Expiration Date: 2023-01-04   

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Search
# Enter product name or category to search: Apple
# Search results:
# Name: Apple, Category: Fruits, Price: 120.0, Quantity: 1, Expiration Date: 2025-01-01   

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Categorize 
# Category: Devices
#   Name: Watch, Price: 20000.0, Quantity: 1, Expiration Date: 2027-04-04
# Category: Fruits
#   Name: Apple, Price: 120.0, Quantity: 1, Expiration Date: 2025-01-01
#   Name: Mango, Price: 150.0, Quantity: 2, Expiration Date: 2023-01-04

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Save
# Enter file path to save inventory: inventory.txt
# Inventory saved successfully.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Load 
# Invalid choice, please try again.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Load
# Enter file path to load inventory: inventory.txt
# Category: Devices
#   Name: Watch, Price: 20000.0, Quantity: 1, Expiration Date: 2027-04-04
# Category: Fruits
#   Name: Apple, Price: 120.0, Quantity: 1, Expiration Date: 2025-01-01
#   Name: Mango, Price: 150.0, Quantity: 2, Expiration Date: 2023-01-04
# Inventory loaded successfully.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Check 
# Category: Devices
#   Name: Watch, Price: 20000.0, Quantity: 1, Expiration Date: 2027-04-04
# Category: Fruits
#   Name: Apple, Price: 120.0, Quantity: 1, Expiration Date: 2025-01-01
# Expired products removed from the inventory.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Remove
# Enter name of product to remove: Watch
# Category: Fruits
#   Name: Apple, Price: 120.0, Quantity: 1, Expiration Date: 2025-01-01
# Product 'Watch' removed from the inventory.

# Inventory Menu:
# 1. Add a product
# 2. Remove a product
# 3. Search for a product
# 4. List all products
# 5. Categorize products
# 6. Check for expired products
# 7. Save inventory to file
# 8. Load inventory from file
# 9. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Check/Save/Load/Exit): Exit
# Exiting the inventory system. Goodbye!