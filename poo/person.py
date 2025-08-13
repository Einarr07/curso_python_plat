class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} I am {self.age} years old")

person = Person("Jaime", 36)
person.greet()

person1 = Person("Ana", 25)
person1.greet()