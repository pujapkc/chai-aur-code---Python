#1. classify the person according to their age

# print("Enter the Age")
# age=int(input())

# if age <13:
#     print("child")
# elif age>13 or age<=19:
#     print("Teenager")
# elif age >20 or age <=59:
#     print("Adult")
# else:
#     print("Senior")

#2 Movie Tickets Pricing

print("Enter the day when you visit the movie theatre")

day = input()

print("Enter your age")

Age = int(input())

# if Age >=18:
#     if day == 'wednesday':
#         ticket = '10$'
#     else:
#         ticket = '12$'

# elif Age<18:
#     if day =='wednesday':
#         ticket = '6$'
#     else:
#         ticket='8$'

# print(f"Ticket pricing is {ticket} ")





#optimized code for the above problem

ticket=12 if Age>=18 else 8

if day == 'wednesday':
    ticket=ticket-2

print(f"Ticket pricing is {ticket} ")


#to exit from a python program use exit()

