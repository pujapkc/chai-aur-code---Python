# name = input("Enter your name\n")
# amount = int(input("Enter the amount to bid\n"))

bid = {}

def Winner_bidder(bid):
    highest_amount = 0

    for bidder in bid:
        bidding_amount = bid[bidder]

        if bidding_amount>highest_amount:
            highest_amount = bidding_amount

    print(f"The winner of the bid is {bidder} with a bid of {highest_amount}")





continue_bidding = True


while continue_bidding:
    name = input("Enter your name\n")
    amount = int(input("Enter the amount to bid\n"))
    bid[name] = amount

    new_bid_or_not = input("Is there any bidder or not\n").lower()

    if new_bid_or_not == 'no':
        continue_bidding = False
        Winner_bidder(bid)

    elif new_bid_or_not == 'yes':
        print("\n" *10)

