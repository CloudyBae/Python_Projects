import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_done = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
   
while not bidding_done:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: "))
  bids[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if other_bidders == "no":
    bidding_done = True
    find_highest_bidder(bidding_record=bids)
  elif other_bidders == "yes":
    os.system("cls")