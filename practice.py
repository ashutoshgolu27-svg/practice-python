# char_count = {}
# for ch in char_count:
#     if ch in char_count:
#         char_count[ch] += 1
#     else:
#         char_count[ch] = 1
# print(char_count)

#find prime numberor not prime numbr

# num = int(input("Enter a number: "))
# if num <= 1:
#     print("Not a Prime Number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")



# Q3.Count and print how many times 'football' appears in list.


# Sports = ['cricket', 'football', 'tennis', 'football', 'hockey']
# count = 0
# for game in Sports:
#     if game == 'football':
#         count += 1
# print("Football appears", count, "times")


# Q4. Find and print the largest and smallest number in a list.
# [8, 2, 15, 1, 9] without using max() and min().


# numbers = [8, 2, 15, 1, 9]
# largest = numbers[0]
# smallest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print("Largest number:", largest)
# print("Smallest number:", smallest)


# Q5. Write a code to print the key of a minimum value from the
# following dictionary.

# Sample :
# Input:{‘math’:89,’phy’:80,’chem’:67,’eng’:75}
# Output:chem

# marks = {'math': 89, 'phy': 80, 'chem': 67, 'eng': 75}
# min_key = None
# min_value = None
# for key, value in marks.items():
#     if min_value is None or value < min_value:
#         min_value = value
#         min_key = key
# print(min_key)

# n=int(input("enter any number"))
# x=0
# y=1
# i=1
# while i<=n:
#     print(x,end=' ')
#     z=x+y
#     x=y
#     y=z
#     i=i+1



# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# s1 = Student("Shubham", 22)


# print(s1.name)
# print(s1.age)


# s1.display()


# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def show(self):
#         print("Brand:", self.brand)

# c1 = Car("BMW")
# c2 = Car("Audi")

# c1.show()
# c2.show()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def details(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)

# e1 = Employee("Shubham", 50000)
# e2 = Employee("Rahul", 60000)

# e1.details()
# e2.details()

# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

# m1 = Mobile("Samsung", 25000)
# m2 = Mobile("Apple", 80000)

# print(m1.brand, m1.price)
# print(m2.brand, m2.price)

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Aman")

# print(s1.name)

# s1.name = "Shubham"   # Update attribute

# print(s1.name)

#count object.........

# class Student:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# s1 = Student("A")
# s2 = Student("B")
# s3 = Student("C")

# print("Total Objects:", Student.count)

#bank account object....

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def show_balance(self):
#         print("Balance:", self.balance)

# acc1 = BankAccount("Shubham", 1000)

# acc1.deposit(500)
# acc1.show_balance()

#laptop object..

# class Laptop:
#     def __init__(self, brand, ram):
#         self.brand = brand
#         self.ram = ram

#     def details(self):
#         print("Brand:", self.brand)
#         print("RAM:", self.ram)

# l1 = Laptop("HP", "8GB")
# l2 = Laptop("Dell", "16GB")

# l1.details()
# l2.details()

#rectangle object

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# r1 = Rectangle(10, 5)

# print("Area =", r1.area())


#book object...

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

# b1 = Book("Python", "Guido")

# print(b1.title)
# print(b1.author)

#object without constructor...

# class Student:
#     pass

# s1 = Student()

# s1.name = "Shubham"
# s1.age = 22

# print(s1.name)
# print(s1.age)

#car object...

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(self.brand, self.model, "started")

# c1 = Car("Toyota", "Fortuner")
# c1.start()

#circle object

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# c1 = Circle(5)

# print("Area =", c1.area())

#student marks...

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def result(self):
#         if self.marks >= 40:
#             print("Pass")
#         else:
#             print("Fail")

# s1 = Student("Shubham", 85)

# print("Name:", s1.name)
# s1.result()

#interview point..

# class Student:
#     pass

# s1 = Student()
# s2 = Student()

# print(id(s1))
# print(id(s2))

#atm object

# class ATM:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal Successful")
#         else:
#             print("Insufficient Balance")

# atm = ATM(5000)

# atm.withdraw(2000)
# print("Balance:", atm.balance)

#fan object


# class Fan:
#     def __init__(self, brand):
#         self.brand = brand

#     def on(self):
#         print(self.brand, "Fan is ON")

# f1 = Fan("Usha")
# f1.on()


#person object...


# class Person:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

# p1 = Person("Shubham", "Pune")

# print(p1.name)
# print(p1.city)


#calculator object

# class Calculator:
#     def add(self, a, b):
#         return a + b

# c1 = Calculator()

# print(c1.add(10, 20))


#movie object 


# class Movie:
#     def __init__(self, name, rating):
#         self.name = name
#         self.rating = rating

#     def show(self):
#         print("Movie:", self.name)
#         print("Rating:", self.rating)

# m1 = Movie("KGF", 9.5)
# m1.show()


#bike object 

# class Bike:
#     def __init__(self, name):
#         self.name = name

# b1 = Bike("Royal Enfield")
# b2 = Bike("Pulsar")

# print(b1.name)
# print(b2.name)

#employee bonus

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def bonus(self):
#         return self.salary * 0.10

# e1 = Employee("Shubham", 50000)

# print("Bonus =", e1.bonus())


#light bulb 

# class Bulb:
#     def turn_on(self):
#         print("Bulb is ON")

#     def turn_off(self):
#         print("Bulb is OFF")

# b1 = Bulb()

# b1.turn_on()
# b1.turn_off()

#student percentage

# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def percentage(self):
#         return self.marks / 500 * 100

# s1 = Student(425)

# print("Percentage =", s1.percentage())

#shopping cart

# class Cart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

# cart = Cart()

# cart.add_item("Laptop")
# cart.add_item("Mouse")

# print(cart.items)

#temperature converter

# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def to_fahrenheit(self):
#         return (self.celsius * 9/5) + 32

# t1 = Temperature(25)

# print(t1.to_fahrenheit())

#counter object

# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1

# c1 = Counter()

# c1.increment()
# c1.increment()

# print(c1.count)

#dog object

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(self.name, "is barking")

# d1 = Dog("Tommy")
# d1.bark()

#laptop price

# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def display(self):
#         print(self.brand, self.price)

# l1 = Laptop("HP", 55000)
# l1.display()


#atm 

# class ATM:
#     def __init__(self, balance):
#         self.balance = balance

#     def check_balance(self):
#         print("Available Balance:", self.balance)

# a1 = ATM(10000)
# a1.check_balance()


#hospital patient

# class Patient:
#     def __init__(self, name, disease):
#         self.name = name
#         self.disease = disease

#     def details(self):
#         print(self.name, "-", self.disease)

# p1 = Patient("Rahul", "Fever")
# p1.details()

#online course

# class Course:
#     def __init__(self, course_name):
#         self.course_name = course_name

#     def start(self):
#         print(self.course_name, "course started")

# c1 = Course("Python")
# c1.start()

#restaurant order

# class Order:
#     def __init__(self, item):
#         self.item = item

#     def place_order(self):
#         print(self.item, "ordered successfully")

# o1 = Order("Pizza")
# o1.place_order()


#method calling another method

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello", self.name)

#     def display(self):
#         self.greet()

# s1 = Student("Shubham")
# s1.display()

#object comparison

# class Test:
#     pass

# t1 = Test()
# t2 = Test()

# print(t1 == t2)

#object inside list

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Aman")
# s2 = Student("Rahul")

# students = [s1, s2]

# for i in students:
#     print(i.name)


#object passed as arguments

class Student:
    def __init__(self, name):
        self.name = name

def show(student):
    print(student.name)

s1 = Student("Shubham")
show(s1)