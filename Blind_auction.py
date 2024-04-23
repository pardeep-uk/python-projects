bids={}
bidding_finishes=True

def find_highest_bidder(bidding_record):
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        highest_bid=0
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid} ")

while bidding_finishes:
    name = input("What is your name: ").lower()
    price = int(input("What is your bid price?$"))
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if should_continue == "no":
        bidding_finishes=False
        find_highest_bidder(bids)

