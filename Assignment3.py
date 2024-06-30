#                                      Assignment - 3
# Design a vehicle rental system using object-oriented programming (OOP) principles in Python. The system should allow users to perform various operations related to managing vehicles and rentals.

# Code
class Vehicle:               #created a class vehicles with attributes
    def __init__(self, vehicle_id, make, model, year, category):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category
# for every attribute we define a fuction
    def get_vehicle_id(self):
        return self.vehicle_id
    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id
    def get_make(self):
        return self.make
    def set_make(self, make):
        self.make = make
    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model
    def get_year(self):
        return self.year
    def set_year(self, year):
        self.year = year
    def get_category(self):
        return self.category
    def set_category(self, category):
        self.category = category
# create another class vahicleRentalSystem and write fuction of the operation needed to perform
class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = []
        self.vehicle_set = set()
        self.vehicle_dict = {}
    def add_vehicle(self, vehicle):
        vehicle_tuple = (vehicle.vehicle_id, vehicle.make, vehicle.model, vehicle.year, vehicle.category)
        if vehicle_tuple not in self.vehicle_set:
            self.vehicles.append(vehicle)
            self.vehicle_set.add(vehicle_tuple)
            print(f"Vehicle {vehicle.vehicle_id}: {vehicle.year} {vehicle.make} {vehicle.model} ({vehicle.category}) added successfully.")
        else:
            print(f"Vehicle {vehicle.vehicle_id}: {vehicle.year} {vehicle.make} {vehicle.model} ({vehicle.category}) is already in the system.")
    def remove_vehicle(self, vehicle_id):
        vehicle_to_remove = None
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                vehicle_to_remove = vehicle
                break
        if vehicle_to_remove:
            self.vehicles.remove(vehicle_to_remove)
            self.vehicle_set.remove((vehicle_to_remove.vehicle_id, vehicle_to_remove.make, vehicle_to_remove.model, vehicle_to_remove.year, vehicle_to_remove.category))
            print(f"Vehicle {vehicle_to_remove.vehicle_id}: {vehicle_to_remove.year} {vehicle_to_remove.make} {vehicle_to_remove.model} ({vehicle_to_remove.category}) removed successfully.")
        else:
            print(f"No vehicle found with ID {vehicle_id}.")
    def search_vehicles(self, search_term):
        results = [vehicle for vehicle in self.vehicles if search_term.lower() in vehicle.make.lower() or search_term.lower() in vehicle.model.lower()]
        if results:
            for vehicle in results:
                print(f"{vehicle.vehicle_id}: {vehicle.year} {vehicle.make} {vehicle.model} ({vehicle.category})")
        else:
            print("No vehicles found matching the search term.")
    def list_vehicles(self):
        if self.vehicles:
            for vehicle in self.vehicles:
                print(f"{vehicle.vehicle_id}: {vehicle.year} {vehicle.make} {vehicle.model} ({vehicle.category})")
        else:
            print("No vehicles in the system.")
    def categorize_vehicles(self):
        self.vehicle_dict.clear()
        for vehicle in self.vehicles:
            if vehicle.category not in self.vehicle_dict:
                self.vehicle_dict[vehicle.category] = []
            self.vehicle_dict[vehicle.category].append(vehicle)
        for category, vehicles in self.vehicle_dict.items():
            print(f"Category: {category}")
            for vehicle in vehicles:
                print(f" - {vehicle.vehicle_id}: {vehicle.year} {vehicle.make} {vehicle.model}")
def main():
    rental_system = VehicleRentalSystem()
# use while loop for menu and thaken choices of user
    while True:
        print("\nVehicle Rental System Menu:")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. Search Vehicles")
        print("4. List All Vehicles")
        print("5. Categorize Vehicles")
        print("6. Exit")
        choice = input("Enter your choice (Add/Remove/Search/List/Categorize/Exit): ")
        if choice == 'Add':
            try:
                vehicle_id = int(input("Enter vehicle ID: "))
                make = input("Enter vehicle make: ")
                model = input("Enter vehicle model: ")
                year = int(input("Enter vehicle year: "))
                category = input("Enter vehicle category: ")
                vehicle = Vehicle(vehicle_id, make, model, year, category)
                rental_system.add_vehicle(vehicle)
            except ValueError:
                print("Invalid input. Please enter the correct details.")
        elif choice == 'Remove':
            try:
                vehicle_id = int(input("Enter vehicle ID to remove: "))
                rental_system.remove_vehicle(vehicle_id)
            except ValueError:
                print("Invalid input. Please enter a valid vehicle ID.")
        elif choice == 'Search':
            search_term = input("Enter search term (make/model): ")
            rental_system.search_vehicles(search_term)
        elif choice == 'List':
            rental_system.list_vehicles()
        elif choice == 'Categorize':
            rental_system.categorize_vehicles()
        elif choice == 'Exit':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

# Output
# PS C:\Users\piyu\OneDrive\Desktop\python> & "C:/Program Files/Python312/python.exe" c:/Users/piyu/OneDrive/Desktop/python/Assignment2.py/3.py

# Vehicle Rental System Menu:
# 1. Add Vehicle
# 2. Remove Vehicle
# 3. Search Vehicles
# 4. List All Vehicles
# 5. Categorize Vehicles
# 6. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Exit): Add
# Enter vehicle ID: 13579
# Enter vehicle make: Mercedes-Benz
# Enter vehicle model: E-Class
# Enter vehicle year:  2022
# Enter vehicle category: Luxury Sedan
# Vehicle 13579: 2022 Mercedes-Benz E-Class (Luxury Sedan) added successfully.

# Vehicle Rental System Menu:
# 1. Add Vehicle
# 2. Remove Vehicle
# 3. Search Vehicles
# 4. List All Vehicles
# 5. Categorize Vehicles
# 6. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Exit): Add
# Enter vehicle ID: 11223
# Enter vehicle make: Subaru
# Enter vehicle model: Outback
# Enter vehicle year: 2021
# Enter vehicle category: Crossover
# Vehicle 11223: 2021 Subaru Outback (Crossover) added successfully.

# Vehicle Rental System Menu:
# 1. Add Vehicle
# 2. Remove Vehicle
# 3. Search Vehicles
# 4. List All Vehicles
# 5. Categorize Vehicles
# 6. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Exit): Add
# Enter vehicle ID: 54321
# Enter vehicle make: Chevrolet
# Enter vehicle model: Silverado
# Enter vehicle year: 2019
# Enter vehicle category: Crossover
# Vehicle 54321: 2019 Chevrolet Silverado (Crossover) added successfully.

# Vehicle Rental System Menu:
# 1. Add Vehicle
# 2. Remove Vehicle
# 3. Search Vehicles
# 4. List All Vehicles
# 5. Categorize Vehicles
# 6. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Exit): Categorize
# Category: Luxury Sedan
#  - 13579: 2022 Mercedes-Benz E-Class
# Category: Crossover
#  - 11223: 2021 Subaru Outback
#  - 54321: 2019 Chevrolet Silverado

# Vehicle Rental System Menu:
# 1. Add Vehicle
# 2. Remove Vehicle
# 3. Search Vehicles
# 4. List All Vehicles
# 5. Categorize Vehicles
# 6. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Exit): List
# 13579: 2022 Mercedes-Benz E-Class (Luxury Sedan)
# 11223: 2021 Subaru Outback (Crossover)
# 54321: 2019 Chevrolet Silverado (Crossover)

# Vehicle Rental System Menu:
# 1. Add Vehicle
# 2. Remove Vehicle
# 3. Search Vehicles
# 4. List All Vehicles
# 5. Categorize Vehicles
# 6. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Exit): Search
# Enter search term (make/model): Subaru
# 11223: 2021 Subaru Outback (Crossover)

# Vehicle Rental System Menu:
# 1. Add Vehicle
# 2. Remove Vehicle
# 3. Search Vehicles
# 4. List All Vehicles
# 5. Categorize Vehicles
# 6. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Exit): Remove
# Enter vehicle ID to remove: 11223
# Vehicle 11223: 2021 Subaru Outback (Crossover) removed successfully.

# Vehicle Rental System Menu:
# 1. Add Vehicle
# 2. Remove Vehicle
# 3. Search Vehicles
# 4. List All Vehicles
# 5. Categorize Vehicles
# 6. Exit
# Enter your choice (Add/Remove/Search/List/Categorize/Exit): Exit
# Exiting the system.