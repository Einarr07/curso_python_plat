class Employee:

    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce_employee(self) -> str:
        return f'Hola soy {self.name} y tengo {self.age} años'

employee1 = Employee('John', 25, 2000.0)
print(employee1.introduce_employee())