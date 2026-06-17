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

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def details(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)

l1 = Laptop("HP", "8GB")
l2 = Laptop("Dell", "16GB")

l1.details()
l2.details()