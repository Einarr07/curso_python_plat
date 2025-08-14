class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def sell(self):
        if self.available:
            self.available = False
            print(f"The car {self.brand} {self.model} was bought")
        else:
            print(f"The car {self.brand} {self.model} was not available")

    def check_available(self):
        return self.available

    def get_price(self):
        return self.price


class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.cars_purchased = []

    def buy_car(self, car):
        if car.check_available():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"Sorry, {car.brand} {car.model} is not available")

    def inquire_car(self, car):
        availability = "available" if car.check_available() else "not available"
        print(f"Car {car.brand} {car.model} is {availability} and how much {car.get_price()}")

class Dealership:

    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"The car {car.brand} {car.model} was added to inventory")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"The customer {customer.first_name} {customer.last_name} was registered")

    def show_available_cars(self):
        print("Available cars:")
        for car in self.inventory:
            if car.check_available():
                print(f"\t- Brand:{car.brand} Model:{car.model} Price:{car.price}")

# Create car instances
car1 = Car("Toyota", "Mustang", 20000)
car2 = Car("Honda", "Civic", 20000)
car3 = Car("Ford", "Mustang", 20000)

# Create customer instances
customer1 = Customer("Armando", "Paredez")
customer2 = Customer("Soria", "Cabezas")

# Create dealership instances and register cars and customers
dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.register_customer(customer1)
dealership.register_customer(customer2)

# Show available cars
dealership.show_available_cars()

# Customer consults a car
customer1.inquire_car(car1)

# Customer buy a car
customer1.buy_car(car1)

# Show available cars
dealership.show_available_cars()

# Customer buy a car what is not available
customer2.buy_car(car1)



