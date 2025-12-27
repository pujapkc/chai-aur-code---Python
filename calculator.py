continue_calculating = True

while continue_calculating:
    first_number = int(input("Enter the first number\n"))

    operation = input("Enter the operation you want to perform \n + \n - \n * \n / \n")

    second_number = int(input("Enter the second number"))

    if operation == '+':
        print(f"{first_number}+{second_number} = {first_number + second_number}")
    elif operation == '-':
        print(f"{first_number}-{second_number} = {first_number - second_number}")
    elif operation == '*':
        print(f"{first_number}*{second_number} = {first_number * second_number}")
    elif operation == '/':
        print(f"{first_number}/{second_number} = {first_number / second_number}")
    else:
        print("Invalid Operator")
        operation = input(
            "Enter the operation you want to perform \n + \n - \n * \n / \n"
        )
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            continue
        
        else:
            break
    break

continue_calculating = False
