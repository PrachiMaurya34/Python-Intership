from menu import Menu, InvalidMenuItemError
from order import Order, InsufficientQuantityError

def main():
    menu = Menu()
    order = Order()

    while True:
        print("\nRestaurant Management System")
        print("1. Add Menu Item")
        print("2. Update Menu Item")
        print("3. Delete Menu Item")
        print("4. Display Menu")
        print("5. Place Order")
        print("6. Generate Receipt")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                menu.add_item(name, price, quantity)
                print("Item added successfully.")
            elif choice == '2':
                name = input("Enter item name: ")
                price = input("Enter new price (leave blank to skip): ")
                quantity = input("Enter new quantity (leave blank to skip): ")
                menu.update_item(name, float(price) if price else None, int(quantity) if quantity else None)
                print("Item updated successfully.")
            elif choice == '3':
                name = input("Enter item name: ")
                menu.delete_item(name)
                print("Item deleted successfully.")
            elif choice == '4':
                menu.display_menu()
            elif choice == '5':
                order.take_order(menu)
                print("Order placed successfully.")
            elif choice == '6':
                order.generate_receipt()
                order.write_orders_to_file()
                print("Receipt generated.")
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")
        except (InvalidMenuItemError, InsufficientQuantityError) as e:
            print(e)

if __name__ == "__main__":
    main()
