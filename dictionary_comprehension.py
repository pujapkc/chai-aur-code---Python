import random

names = ['james','tim','tom']

new_dict = {name:random.randint(1,100) for name in names}

print(new_dict)

passed_students = {student:score for (student,score) in new_dict.items() if score >60}

print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

list_name = sentence.split()

print(list_name)