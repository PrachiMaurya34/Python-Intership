import os
import json

class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

class Menu:
    def __init__(self):
        self.items = {}
        self.read_menu_from_file()

    def add_item(self, name, price, quantity):
        if name in self.items:
            raise InvalidMenuItemError(f"Item '{name}' already exists in the menu.")
        self.items[name] = MenuItem(name, price, quantity)
        self.write_menu_to_file()

    def update_item(self, name, price=None, quantity=None):
        if name not in self.items:
            raise InvalidMenuItemError(f"Item '{name}' does not exist in the menu.")
        if price is not None:
            self.items[name].price = price
        if quantity is not None:
            self.items[name].quantity = quantity
        self.write_menu_to_file()

    def delete_item(self, name):
        if name not in self.items:
            raise InvalidMenuItemError(f"Item '{name}' does not exist in the menu.")
        del self.items[name]
        self.write_menu_to_file()

    def display_menu(self):
        for item in self.items.values():
            print(f"{item.name}: ${item.price:.2f} (Quantity: {item.quantity})")

    def read_menu_from_file(self):
        if os.path.exists('menu.txt'):
            with open('menu.txt', 'r') as file:
                self.items = {name: MenuItem(**data) for name, data in json.load(file).items()}
        else:
            self.items = {}

    def write_menu_to_file(self):
        with open('menu.txt', 'w') as file:
            json.dump({name: item.to_dict() for name, item in self.items.items()}, file)

class InvalidMenuItemError(Exception):
    pass