import random
import os
from game_data import data
from logo import hl_logo, vs
os.system("cls")
print(hl_logo)

def game():
    global score
    global a
    global b
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    print(f"Compare A : {a['name']}, {a['description']}, from {a['country']}{vs}\n\nAgainst B : {b['name']}, {b['description']}, from {b['country']}")
    
    compare()
    if input("Who has more followers? Type 'A' or 'B' : ") == win:
        score += 1
        os.system("cls")
        print(hl_logo)
        print(f"Great!!! You're right!!!  Current Score = {score}\n")
        if win == "A":
            b = a
        game()
    else:
        os.system("cls")
        print(hl_logo)
        print(f"Sorry!!! You're wrong!!!  Final Score = {score}\n")
        score = 0
        if input("Do you want to start the game again? (y/n) : ") == "y":
            os.system("cls")
            print(hl_logo)
            game()
        else:
            print("\n\n***** Thankyou *****")

def compare():
    global win
    win = "B"
    if a["follower_count"] > b["follower_count"]:
        win = "A"

score = a = 0
b = random.choice(data)
game()
