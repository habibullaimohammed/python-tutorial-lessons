""" Loops:
    A loop can happen ones, it can happen twice and can happen infinite times
"""

# While loops

# while condition:
#     statement
#     statement
# else:
#     statement

# A pattern of right angle triangle using $
# no_of_rows = 1
# while no_of_rows <= 6:
#     print(no_of_rows * '$')
#     no_of_rows += 1

# Print a single char of a string
# name = 'habib'
# count = 0
# while count < len(name):
#     print(name[count])
#     count += 1


# For Loop
# Range function is commonly used with for loop,
# and it generates a sequence of number 'range(start, stop, step_size)'


# for iter in sequence:
#     statement
#
# for i in range(1, 10, 2):
#     print(i)

# names = ['John', 'Smith', 'Habib', 'Joe']
#
# for name in names:
#     print(name)

# name = 'Habib'
#
# for letter in name:
#     print(letter)

# name = 'Mohammed'
# for i in range(len(name)):
#     print(name[i])

# name = 'Habib'
# for i, char in enumerate(name):
#     print(i, char)

"""Difference btw for loop and while loop
For loop - Number of the element we need to loop over are now before hand.
While loop - Number of elements not known before hand
"""


# Tuples

# my_tuple = (1, 2, 3, 2)
# print(my_tuple)

# Set
# Set are unordered
# my_set = {1, 2, 2, 3, 4}
# print(my_set)
#
# # Set in math
# my_set2 = {1, 2, 5, 6, 7, 8}
# print(my_set.intersection(my_set2))
# print(my_set & my_set2) # also intersection
#
# print(my_set.union(my_set2))
# print(my_set | my_set2) # union
#
# print(my_set.difference(my_set2))
# print(my_set - my_set2) # difference

# Dictionary: is a key value pair

# my_dict = {'id': 80, 'name': 'habib'}
# print(my_dict.get('id', 0)) # Get the value base on a key and return None by default when no key is found
# print(my_dict.values()) # Get only the value in the dictionaries
#
# for i in my_dict:

#     print(i)
#
# for key, val in my_dict.items():
#     print(key, val)


# Function

# def my_function():
#     print("Hello from inside a function")
#
# my_function()

# def hello_name(name):
#     print(f'Hello {name}')
#
#  Function argument have two types named and position argument
#
# hello_name('Habib')
# hello_name(name='John')  # To work with position argument

# If you put a comma / at the end of argument the function well only accept positional argument
# def example(age, level, /):
#     print(age, level, sep='\n')
#
#
# example(19, 67)
#  If you put a comma * at the end of argument the function well only accept named argument
# def example(*, name, age):
#     print(name, age)
#
# example(name='habib', age=77)

# The Default value can also be set on functions
# def example(name, age=18):
#     print(name, age)
#
# example('Habib', 19)
# example('Habib')

# Arbitrary argument: allows you to pass as many argue as you need,
# Using double ** means you will need to use key word e.g **kid: print(first='habib', last='mohammed')
# def sibling_kids(name, *kid):
#     print(f'User\'s name {name}')
#     print(kid)
#
#
# sibling_kids('habib', 'awwal', 'fawwaz')

# Functions call use the return keyword to return a value

print()