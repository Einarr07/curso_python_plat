class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)
        print(f"My age is {self.age}")
        print("-------------------------")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"I'm student my name is {self.name} and my id is {self.student_id}")

student = Student("Alice", 24, 21)
person = Person("John", 21)

person.greet()
student.greet()
