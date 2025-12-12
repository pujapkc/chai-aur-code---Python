import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

pass_alpha  = int(input("Enter the length of alphabets you would like to keep in a password\n"))
pass_num = int(
    input("Enter the length of numbers you would like to keep in a password\n")
)
pass_symbol = int(
    input("Enter the length of symbol you would like to keep in a password\n")
)

password_list = []

for char in range(0,pass_alpha):
    password_list+=random.choice(letters)

for char in range(0,pass_num):
    password_list+=random.choice(numbers)

for char in range(0,pass_symbol):
    password_list+=random.choice(symbols)

random.shuffle(password_list)

password = ""

for char in password_list:
    password+=char

# Random.shuffle() function cannot directly works with strings as strings are immutable but it can work with list

# random.shuffle(password)

print(f"Your password is {password}")
