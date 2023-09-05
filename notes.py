# This File will be used as notes for the basics of python
# There is a lot in this file, you should add, subtract, change things as needed to help fully understand the process.
# Mr. Berg will be going over all parts, but will not be grading anything in this file

# types

from operator import truediv


# when defining a variable in python you put the varialbe name : then the data type for example name: str = "sam".
# There are several types of data in python str for strings, int for whole numbers, float for decimals, bool for true or false.
# list are things you use to hold nultiple data values at the same time to make one you just put the name of the list = [things in the list seperated by comas]


# # str defining the variable
# y = "I love Computer Science!"

# # numbers and floats
# mynum = 47
# anothernum = 47.7
# print(type(mynum))
# print(type(anothernum))

# # bools - True, False
# flag = false
# print(flag)
# flag = true
# print(flag)

# # lists - can hold a list of items of any type
lane_tech = ["chicago", "high school", 1908, 60618, "addison/western"]
# print(lane_tech.reverse()) # reverse is a function that works with list that is used with print so that the list is printed from backwards to forwards
# print(lane_tech)# . reverse is also permanant unless you do .reverse again
# lane_tech.pop.(0) # takes out the index value that ic showed
# print(lane_tech)


# Indices
#print(lane_tech[1]) # this makes it so that only the first index value is printed
#print(lane_tech[-1])
#print(lane_tech[len(lane_tech)-1])

# # Slices
# print(lane_tech[1:3]) This makes it so that it only prints the index values 1-3
# print(lane_tech[:3])
# print(lane_tech[1:])
# print(lane_tech[:])

# # Functions

# # defining a function
# def hello_world():
#     print("hello world")

# # calling a function
# hello_world()

def add_two(n: int): # the n is the name of a variable that can be used inside the function the value for n is added when you call the function

    return n+2
    
#     Args: 
#         n - a number
    
#     Returns:
#         the input number + 2
#     """
#     return n + 2

assert add_two(5) == 7, "add_two with input 5 test"
assert add_two(-2) == 0, "add_two with input -2 test"
assert add_two(0) == 2, "add_two with input 0 test"

# # Loops

# # For Loop Template 1
# # do something for each item in a list
# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# for el in lst:
#     print(el)

# # For Loop Template 2
# # do something n times
# for i in range(5):
#     print("Intro to AI")

# # For Loop Template 3
# # do something for each item in a list but we care about the index
# for r in range(len(lst)):
#     if lst[r] == 'b':
#         lst[r] = 'c'

# print(lst)

# # Dictionaries

# dict = {"name": "rob", "age": 30}
# print(dict["age"])

# # Random
# import random

# food = ['pizza', 'carrots', 'eggs']
# dinner = random.choice(food)
# print(dinner)

# # f String
# age = 25
# # print("Mary is " + age + " years old")
# print(f"Mary is {age} years old")


