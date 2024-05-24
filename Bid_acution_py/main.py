import os
from logo import logo_style
temp = input("***** Welocome to Acution *****\nPress Enter to proceed !!!")
os.system("cls")
print(logo_style, "\n\n")
bid = {"":0}
next_bidder = winner = ""

def bid_acution(bid, next_bidder, winner):
    os.system("cls")
    print(logo_style, "\n\n")
    bidder = input("Enter your name: ")
    bid[bidder] = int(input("Enter the bid amount: $"))
    if bid[bidder] > bid[winner]:
        winner = bidder
    next_bidder = input("Do we have anyother bidders? Type 'yes' or 'no'\n")
    if next_bidder == "yes":
        winner = bid_acution(bid, next_bidder, winner)
    return winner
winner = bid_acution(bid, next_bidder, winner)

print(f"The winner is {winner} with the bid of {bid[winner]}")

# import os
# from logo import logo_style
# temp = input("***** Welcome to Acution *****\nPress any key to proceed !!!")
# os.system("cls")
# print(logo_style, "\n\n")
# accution = "yes"
# name_list = []
# amount_list = []
# while accution == "yes":
#     name = name_list.append(input("What is your name: "))
#     amount = amount_list.append(int(input("What amount would you like to bid: $")))
#     accution = input("Do we have any other bidders? Type 'yes' or 'no'")
#     if accution == "yes":
#         os.system("cls")
#         print(logo_style, "\n\n")
#     else:
#         break

# print(f"The winner is {name_list[amount_list.index(max(amount_list))]} with the bid of ${max(amount_list)}")