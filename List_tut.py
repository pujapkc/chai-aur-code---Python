tea_varities = ["Green","Masala","White","Pink"]

#slicing is same like string

print(tea_varities[1:1])

#insertion using slicing

tea_varities[1:1] = 'test','test'

print(tea_varities)

#deletion using slicing

tea_varities[1:3] = []

print(tea_varities)


#list comprehension

print(range(10)) #it gives us the range of values from 0 to n-1

squared_num = [x**2 for x in range(10)]

print(squared_num)