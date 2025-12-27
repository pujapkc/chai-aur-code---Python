def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
    else:
        print("Invalid operator")
        return None


continue_calculating = True

first_number = int(input("Enter the first number: "))

while continue_calculating:

    operation = input("Enter the operation you want to perform:\n+\n-\n*\n/\n")

    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operator")
        continue

    second_number = int(input("Enter the second number: "))

    result = calculate(first_number, second_number, operation)
    print(f"Result = {result}")

    choice = input("Type 'y' to continue calculating or 'n' to exit: ").lower()

    if choice == "y":
        first_number = result  # 👈 reuse result
    else:
        continue_calculating = False
