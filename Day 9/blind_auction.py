import art
print(art.logo)
# TODO-1: Ask the user for input
bids = {}
# TODO-3: Whether if new bids need to be added
# TODO-2: Save data into dictionary {name: price}
def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of  $ {highest_bid}")


# TODO-4: Compare bids in dictionary
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("what is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? y/n: \n")
    if should_continue == "n":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "y":
        print("\n" * 20)