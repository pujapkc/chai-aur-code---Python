name = "puja"

# to print first character
print(name[0])

# slicing

num_list = "0123456789"

print(num_list[:])

# hopping

print(num_list[0:7:3])

# split - split the string

chai = "lemon, ginger, Masala, mint"

print(chai.split())

# find()- to find the start position of any character or word and if it
# is not present then it will send -1 as output

print(chai.find("ch"))

print(chai.find("Masala"))

# count - to count how many times a string has come

chaii ="Masala Chai Chai Chai"

print(chaii.count("Chai"))

# placeholder

Chai_type = "Masala Tea"
quantity = 2
order = "I Ordered {} cups of {} "

print(order.format(quantity,Chai_type))

# conversion of list to string

List = ["Apple","Mango","Banana"]

print(", ".join(List))


# to find length of a string

print(len(Chai_type))


# to print each character of a string

for letter in Chai_type:
    print(letter)

#raw string

chai = "Masala\nchai"

print(chai) #general case

chai1 = r"Masala\nchai"

print(chai1)

#drive = r"c:\user\pwd\" - will give an error

drive = r"c:\user\pwd"

print(drive)


