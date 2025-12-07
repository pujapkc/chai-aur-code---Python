print("Welcome to Tip Calculator")

total_bill= input("What was the total bill")

tip= input("How much tip would you like to give - 10,12,15")

people = input("How many people to split the bill?")

final_bill = total_bill+tip

pay_amount = final_bill/5

full_bill = round(pay_amount)

print(f"Each person should pay {full_bill}")

