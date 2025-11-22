# in python everything is an object

# taking  user input in list which is same like array in python

# input() treats all the inputs as a single string

# to convert any input from string to other data type we need to explicitely convert them

str = input("Enter a string  ")

num = int(input("Enter a number "))

print(type(num))# everything is an object that is why when we write type() so it also
# an object and it shows that the variable is of which class type


# using input() and list comprehension for integers and float
num_list = [int(item) for item in input("Enter numbers to check if they are positive or not with spaces").split()]

print(num_list)

# Taking multiple inputs in a loop:
# If you need to collect a specific number of elements, or if each element needs to be entered on a separate line, you can use a loop.
# using append function
num_items = int(input("Enter the number of inputs"))

nums = []

for i in range(num_items):
    num = input(f"Enter item {i+1}  - ")
    nums.append(num)

print("Entered items: ",nums)    


# using map() and list() for numeric inputs
user_input = list(map(int,input("enter the numbers with spaces").split()))

print(user_input)


# write - python loops_problems.py Puja on powershell and you will get the output
# for CMD input
import sys

if len(sys.argv) > 1:
    message = sys.argv[1]
    print(f"Received message: {message}")
else:
    print("No message provided as argument.")
