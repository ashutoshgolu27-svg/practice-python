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

# class Student:
#     def __init__(self, name):
#         self.name = name

# def show(student):
#     print(student.name)

# s1 = Student("Shubham")
# show(s1)

#object returned as function

# class Student:
#     def __init__(self, name):
#         self.name = name

# def create_student():
#     return Student("Shubham")

# s1 = create_student()

# print(s1.name)

#interview object

# class Demo:
#     pass

# d1 = Demo()
# d2 = Demo()

# print(id(d1))
# print(id(d2))

#constructor method

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)

# e1 = Employee("Shubham", 50000)
# e1.show()

#two object different data

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Aman")
# s2 = Student("Rahul")

# print(s1.name)
# print(s2.name)

#object attribute delete


# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Shubham")

# print(s1.name)

# del s1.name

#class variable and object

# class Student:
#     school = "ABC School"

# s1 = Student()
# s2 = Student()

# print(s1.school)
# print(s2.school)

#change object variable

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Aman")

# print(s1.name)

# s1.name = "Shubham"

# print(s1.name)

#object counter

# class Student:
#     count = 0

#     def __init__(self):
#         Student.count += 1

# s1 = Student()
# s2 = Student()
# s3 = Student()

# print(Student.count)

#if statement find greater value

# x = 10

# if x > 5:
#     print("x is greater than 5")

#else statement find smaller value

# x = 2

# if x > 5:
#     print("Greater")
# else:
#     print("Smaller")

#elif statement

# x = 0

# if x > 0:
#     print("Positive")
# elif x == 0:
#     print("Zero")
# else:
#     print("Negative")

#for loop

# for i in range(5):
#     print(i)

#while loop

# i = 1

# while i <= 3:
#     print(i)
#     i += 1

#break method 

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

#continue iteration

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)


#greet method

# def greet():
#     print("Hello")

# greet()

#slice 

# a = [10, 20, 30, 40, 50]
# print(a[1:4])


#find python indexing with slicing

# s = "PYTHON"
# print(s[1:4])

#find 2nd and 4th element with slicing

# l = [5, 10, 15, 20, 25, 30]
# print(l[1:4])

#full list copy

# l = [1, 2, 3, 4]
# x = l[:]
# print(x)

#find 2 to last element

# l = [10, 20, 30, 40, 50]
# print(l[2:])

#find alternative element


# l = [10, 20, 30, 40, 50, 60]
# print(l[::2])

#revrese slicing

# l = [1, 2, 3, 4, 5]
# print(l[::-1])


#how to reverse string 

# s = "python"
# print(s[::-1])

#find alphabet words

# s = "ABCDEFGHIJ"
# print(s[1:8:2])

#find odd index element

# a = [10,20,30,40,50,60]
# print(a[1::2])

#how to get last three element 

# a = [1,2,3,4,5,6]
# print(a[-3:])

#negative index count from end

# a = [10,20,30]
# print(a[-1])

#reverse last 2 element

# a = [1,2,3,4,5,6]
# print(a[::-2])

#can slicing use tuple

# t = (10,20,30,40)
# print(t[1:3])

#replacement elemnt using slicing

# numbers = [10,20,30,40,50]

# numbers[1:3] = [100,200]

# print(numbers)

#delete element using slicing

# numbers = [10,20,30,40,50]

# del numbers[1:4]

# print(numbers)

#slice a tuple

# t = (1,2,3,4,5)

# print(t[1:4])

#empty slice

# numbers = [10,20,30]

# print(numbers[2:1])

#addition to two nos..

# a = 10
# b = 20

# print("Sum =", a + b)

#user input

# name = input("Enter your name: ")
# print("Welcome", name)

#largest number

# a = 30
# b = 50

# if a > b:
#     print(a)
# else:
#     print(b)

#multiply table

# num = 5

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

#sum of 1st 10 no 

# total = 0

# for i in range(1, 11):
#     total += i

# print(total)

#list example

# fruits = ["Apple", "Banana", "Mango"]

# print(fruits)
# print(fruits[1])

#fibonacci series

# a = 0
# b = 1

# for i in range(10):
#     print(a, end=" ")
#     a, b = b, a + b

#count vowels

# text = "Python"

# count = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1

# print(count)

#factorials

# num = 5
# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print(fact)

#function with arguments

# def add(a, b):
#     return a + b

# print(add(10, 20))


#set examples

# numbers = {1, 2, 3, 2, 1}

# print(numbers)

#list insert

# numbers = [10, 20, 40]

# numbers.insert(2, 30)

# print(numbers)

#inheritance

# class Animal:
#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     pass

# obj = Dog()
# obj.sound()

#list comprehension

# square = [x*x for x in range(5)]

# print(square)

#enumerate

# fruits = ["Apple", "Banana"]

# for i, fruit in enumerate(fruits):
#     print(i, fruit)

#zip function

# names = ["A", "B"]
# marks = [90, 80]

# print(list(zip(names, marks)))

#swap two numbers

# a = 10
# b = 20

# a, b = b, a

# print(a, b)

#find max num

# a = 15
# b = 30

# print(max(a, b))

#sum of list

# numbers = [10, 20, 30, 40]

# print(sum(numbers))

#square number

# for i in range(1, 6):
#     print(i ** 2)

#check data types

# x = 25.5

# print(type(x))

#count list elements

# fruits = ["Apple", "Banana", "Mango", "Orange"]

# print(len(fruits))

#random number 

# import random

# print(random.randint(1, 10))

#remove duplicates

# numbers = [1, 2, 2, 3, 4, 4]

# print(list(set(numbers)))

#cube numbers

# for i in range(1, 6):
#     print(i ** 3)

#check even or odd numbers

# num = 12

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#largest of three number

# a = 10
# b = 25
# c = 15

# print(max(a, b, c))

#check positive negative or zero

# num = -8

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

#find ASCII value

# print(ord('A'))

#generate random float

# import random

# print(round(random.random(), 2))

#check palindrom

# text = "madam"

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#split string

# text = "Python is Easy"

# print(text.split())

#join strings
# words = ["Python", "is", "Easy"]

# print(" ".join(words))

#count occurance in lists

# numbers = [1, 2, 2, 3, 2, 4]

# print(numbers.count(2))

#convert string into integer

# num = "250"

# print(int(num))

#check leap year

# year = 2024

# if year % 4 == 0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")

#print nu 10 to 01

# for i in range(10, 0, -1):
#     print(i)

#sum of first 10 number

# total = 0

# for i in range(1, 11):
#     total += i

# print(total)

#check prime no or not prime

# num = 17

# for i in range(2, num):
#     if num % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")

# num = 987654
# count = 0

# while num > 0:
#     count += 1
#     num //= 10

# print(count)

#check armstrong or not number

# num = 153

# total = sum(int(digit) ** 3 for digit in str(num))

# if total == num:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong")

#find factor

# num = 12

# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

#find common element

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# print(list(set(a) & set(b)))

#merge two lists

# list1 = [1, 2]
# list2 = [3, 4]

# print(list1 + list2)

#count characters

# text = "Python"

# for ch in text:
#     print(ch)

#check strings start with

# text = "Python Programming"

# print(text.startswith("Python"))

#check string end with

# text = "Python.py"

# print(text.endswith(".py"))

#remove spaces

# text = "  Hello Python  "

# print(text.strip())

#find index

# text = "Python"

# print(text.index("h"))

#dictionary key

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Delhi"
# }

# print(student.keys())

#dictionary value

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Delhi"
# }

# print(student.values())

#dictionary key
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Delhi"
# }

# print(student.keys())

#file write

# with open("demo.txt", "w") as file:
#     file.write("Hello")
# print("File Created")

#exception handling

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")

#inheritance

# class Animal:
#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     pass

# obj = Dog()
# obj.sound()

#tuple

# data = (10, 20, 30)

# print(data[1])

#dictionary
# student = {
#     "Name": "Shubham",
#     "Age": 25
# }

# print(student["Name"])

#lambda func

# square = lambda x: x*x

# print(square(5))

#exceptional handling

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

#file handling

file = open("demo.txt", "w")

file.write("Hello Python")

file.close()