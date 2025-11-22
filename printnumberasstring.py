print("Enter the number until which you want to print numbers")
n=int(input())

for i in range(1, n + 1):
    print(i, end="")


# print() adds a newline (\n) after each output.
# end="" changes that behavior so nothing is added after printing each number (no space, no newline).
