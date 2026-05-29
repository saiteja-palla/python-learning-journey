"""
Secret Auction
--------------
A blind auction program where the highest bidder wins.

Rules:
- Collect name and bid from each bidder
- Store in dictionary: bid_dict[name] = price
- Clear screen between bidders using print("\n" * 20)
- After all bids, find winner using max() or manual loop
- Print winner's name and winning bid amount

"""

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bid_dict = {}
repeat = True

while repeat:
    name = input("What's your name? ")
    price = int(input("What's your price? $"))
    bid_dict[name] = price
    repeat = input("Are there any other bidders <yes, no>? ").lower()
    if repeat == "yes":
        repeat = True
        print("\n" * 20)
    else:
        repeat = False

# Method 1 — manual loop
maxbid = 0
winner = ''
for key in bid_dict:
    if bid_dict[key] > maxbid:
        maxbid = bid_dict[key]
        winner = key

# Method 2 — Pythonic one liner
# winner = max(bid_dict, key=bid_dict.get)
# maxbid = bid_dict[winner]

print(f"The winner is: {winner} at a bid of ${maxbid}")