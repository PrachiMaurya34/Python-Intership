import os
import json
from menu import Menu, InvalidMenuItemError

class Order:
    def __init__(self):
        self.items = []
        self.total = 0
        self.read_orders_from_file()

    def take_order(self, menu):
        while True:
            name = input("Enter the menu item name (or 'done' to finish): ").strip()
            if name.lower() == 'done':
                break
            try:
                if name not in menu.items:
                    raise InvalidMenuItemError(f"Item '{name}' not found in menu.")
                quantity = int(input("Enter quantity: "))
                if quantity > menu.items[name].quantity:
                    raise InsufficientQuantityError(f"Not enough quantity for '{name}'.")
                menu.items[name].quantity -= quantity
                self.items.append((name, menu.items[name].price, quantity))
                menu.write_menu_to_file()
            except InvalidMenuItemError as e:
                print(e)
            except InsufficientQuantityError as e:
                print(e)

    def calculate_total(self):
        self.total = sum(price * quantity for name, price, quantity in self.items)
        return self.total

    def generate_receipt(self):
        print("\nReceipt:")
        for name, price, quantity in self.items:
            print(f"{name}: ${price:.2f} x {quantity} = ${price * quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

    def read_orders_from_file(self):
        if os.path.exists('orders.txt'):
            with open('orders.txt', 'r') as file:
                self.items = json.load(file)

    def write_orders_to_file(self):
        with open('orders.txt', 'w') as file:
            json.dump(self.items, file)

class InsufficientQuantityError(Exception):
    pass
