numbers  = [1,2,3]

new_numbers = [n+1 for n in numbers]

print(new_numbers)

range_list = [num*2 for num in range(1,5)]

print(range_list)

names = ['Puja','Prajwal','Vivek']

short_names= [name for name in names if len(name)>3]

print(short_names)