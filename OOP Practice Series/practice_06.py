#1. Using self Assignment

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student = Student("Kounain", 90)
student.display()

#2. Using cls Assignment

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Number of objects: {cls.count}")

obj1 = Counter()
obj2 = Counter()
Counter.display_count()

#3. Public Variables and Methods Assignment

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Car started")

car = Car("Civic,Fortuner")
print(car.brand)
car.start()

#4. Class Variables and Class Methods Assignment

class Bank:
    bank_name = "Meezan Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank1 = Bank()
bank2 = Bank()
print(bank1.bank_name)  
Bank.change_bank_name("Bank AL Habib")
print(bank2.bank_name)  

5#. Static Variables and Static Methods Assignment

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(2, 3)
print(result)  

#6. Constructors and Destructors Assignment

class Logger:
    def __init__(self):
        print("Logger initialized")

    def __del__(self):
        print("Logger destroyed")

logger = Logger()
del logger


#7. Access Modifiers Assignment

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

employee = Employee("Sara", 50000, "123-45-6789")
print(employee.name)  
print(employee._salary)  
try:
    print(employee.__ssn)  
except AttributeError:
    print("Error: cannot access private variable")

# 8. The super() Function Assignment

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher = Teacher("Hamza Ali", "Biology")
print(teacher.name)  
print(teacher.subject)  

#9. Abstract Classes and Methods Assignment

from abc import ABC, abstractmethod
from ast import main

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 5)
print(rectangle.area())  


#10. Instance Methods Assignment

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy", "Golden Retriever")
dog.bark()  


#11. Class Methods Assignment

class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

book1 = Book()
book2 = Book()
print(Book.get_total_books())  


#12. Static Methods Assignment

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

fahrenheit = TemperatureConverter.celsius_to_fahrenheit(30)
print(fahrenheit)  


#13. Composition Assignment

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start_car()

#14. Aggregation Assignment

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

# Test the classes
emp1 = Employee("Ali")
dept = Department("HR")
dept.add_employee(emp1)
print(dept.employees[0].name) 


#15. Method Resolution Order (MRO) and Diamond Inheritance Assignment

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Test the classes
d = D()
d.show() 
print(D.mro())  


#16. Function Decorators Assignment

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Test the decorator
say_hello("Kounain")


#17. Class Decorators Assignment

def add_greeting(cls):
    class Wrapper(cls):
        def greet(self):
            return "Hello from kounain's Decorator!"
    return Wrapper

@add_greeting
class Person:
    pass

# Test the decorator
person = Person()
print(person.greet()) 


#18. Property Decorators Assignment

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Test the class
product = Product(100)
print(product.price)  
product.price = 150
print(product.price)  
del product.price
try:
    print(product.price)
except AttributeError:
    print("Price attribute deleted")


#19. callable() and call() Assignment

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Test the class
multiplier = Multiplier(3)
print(multiplier(5))  
print(callable(multiplier))  


#20. Creating a Custom Exception Assignment

class InvalidAgeError(Exception):
    """Custom exception for invalid age"""
    pass

def check_age(age):
    """Check if age is valid (20 or above)"""
    if age < 20:
        raise InvalidAgeError("Age must be 20 or above")
    else:
        print("Age is valid")

# Test the function
try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    check_age(18)
except InvalidAgeError as e:
    print(f"Error: {e}")


#21. Make a Custom Class Iterable Assignment

class Countdown:
    """Custom class for countdown iterator"""
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Test the class
countdown = Countdown(5)
for num in countdown:
    print(num)

#Completed  by KOUNAIN AFTAB:)

print("Project completed by KOUNAIN AFTAB:)")

if __name__ == "__main__":
    main()

