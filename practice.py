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

n=int(input("enter any number"))
x=0
y=1
i=1
while i<=n:
    print(x,end=' ')
    z=x+y
    x=y
    y=z
    i=i+1
