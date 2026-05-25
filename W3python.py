# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# import random

# print(random.randrange(1, 10))

# print("It's alright")
# print("He is called 'Johnny'")
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# # print(a)
# a = "Hello, World!"
# print(a[2])
# for x in "banana":
# #   print(x)
# txt = "The best things in life are !"
# print("free" in txt)
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("expensive" not in txt)
# a = "Hello, World!"
# print(a.upper())
# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)
# txt = f"The price is {20 * 59} dollars"
# print(txt)
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
# #   print("NO!")
# x = 200
# print(isinstance(x, int))
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# # //	Floor division	x // y
# x = 12
# y = 5

# print(x / y)

# x = 5
# y = 3

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)
# x = 5

# print(1 < x < 10)

# print(1 < x and x < 10)
# x = 5
# hello world 
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
# sum1 = 100 + 50      # 150 (100 + 50)
# sum2 = sum1 + 250    # 400 (150 + 250)
# sum3 = sum2 + sum2   # 800 (400 + 400)
# print(sum1)
# print(sum2)
# print(sum3)
# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# # print(x // y)
# numbers = [1, 2, 3, 4, 5]

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)

# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
# x = [1, 2, 3]
# y = [1, 2, 3]

# print(x == y)
# print(x is y)
# fruits = ["apple", "banana", "cherry"]

# print("banana" in fruits)
# text = "Hello World"

# print("H" in text)
# print("hello" in text)
# print("z" not in text)

# Operator	Name	Description	Example	Try it
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
# print(100 + 5 * 3)
# print(5 + 4 - 7 + 3)
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
# mylist = ["apple", "banana", "cherry"]
# mylist.insert(1,"davai")
# print(mylist)
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])