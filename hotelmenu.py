menu = {
    'pizza':40,
    'pasta':50,
    'coffee':60
}

print("Welcome to Puja Restaurent")

print(" pizza : Rs 40 \n pasta : Rs 50 \n coffee : Rs 60")

order_total=0

item_1 = input("Enter the first item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your order for {item_1} is added in the cart")
else:
    print(f"{item_1} is not available in menu")


another_order = input("Do you want to order another item (Yes/No)")

if another_order  == "Yes":
        item_2 = input("Enter the name of second item")

        if item_2 in menu:
            order_total+= menu[item_2]
            print(f"{item_2} has been added to cart")
        else:
            print(f"{item_2} is not available")   


print(f"The total amount to be paid is {order_total}")             