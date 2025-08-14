class Vehicle:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.brand} {self.model} was purchased successfully.")
        else:
            print(f"{self.brand} {self.model} is not available.")

    def check_available(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("This method is not implemented.")

    def stop_engine(self):
        raise NotImplementedError("This method is not implemented.")

class Car(Vehicle):
    def start_engine(self):
        if self.is_available:
            print(f"The car {self.brand} engine is starting.")
        else:
            print(f"The car {self.brand} is not available to start.")

    def stop_engine(self):
        if self.is_available:
            print(f"The car {self.brand} engine is stopped.")
        else:
            print(f"The car {self.brand} is not available to stop.")

class Bike(Vehicle):
    def start_engine(self):
        if self.is_available:
            print(f"The bike {self.brand} engine is starting.")
        else:
            print(f"The bike {self.brand} is not available to start.")

    def stop_engine(self):
        if self.is_available:
            print(f"The bike {self.brand} engine is stopped.")
        else:
            print(f"The bike {self.brand} is not available to stop.")

class Truck(Vehicle):
    def start_engine(self):
        if self.is_available:
            print(f"The truck {self.brand} engine is starting.")
        else:
            print(f"The truck {self.brand} is not available to start.")

    def stop_engine(self):
        if self.is_available:
            print(f"The truck {self.brand} engine is stopped.")
        else:
            print(f"The truck {self.brand} is not available to stop.")

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Sorry, this vehicle {vehicle.brand} is not available")

    def inquire_vehicles(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Available"
        else:
            availablity = "Not available"
        print(f"The {vehicle.brand} is {availablity} and costs {vehicle.get_price()} are available.")

class Dealership:

    def __init__(self):
        self.invetory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.invetory.append(vehicle)
        print(f"The vehicle {vehicle.brand} is add to inventory")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"The customer {customer.name} was added")

    def show_available_vehicles(self):
        print(f"The available vehicle: ")
        for vehicle in self.invetory:
            if vehicle.check_available():
                print(f"✅ The car {vehicle.brand} is available by {vehicle.get_price()}")
            else:
                print(f"❌ The car {vehicle.brand} is not available")

car1 = Car("Toyota", "Pichirilo", 2000)
bike1 = Bike("Yahama", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Pedro")
customer2 = Customer("Domenica")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

# Vehicles available
dealership.show_available_vehicles()

# Customer consult a car
customer1.inquire_vehicles(car1)

# Purchase car
customer1.buy_vehicle(car1)

# vehicles available
dealership.show_available_vehicles()
