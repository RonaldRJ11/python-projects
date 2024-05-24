import random
import os
from logo import game_logo

def new_game(user, computer):
    os.system("cls")
    print(game_logo[0])
    user = [random.randint(2,11) for i in range(2)]
    computer = [random.randint(2,11) for j in range(2)]
    game(user, computer)

def game(user, computer):
    
    print(f"""your cards {user}, current score : {sum(user)}
computer's first card : {computer[0]}\n\n""")
    
    temp = input("type 'y' to get another card or 'n' to pass: ")
    if temp == "y":
        user.append(random.randint(1,10))
        if sum(user) <= 21:
            game(user, computer)
        else:
            
            print(f"""your final hand {user}, your final score : {sum(user)}
computer's final hand {computer}, copmuter final score : {sum(computer)}\n\n
You went over.\n{game_logo[2]}\n\n""")
            
            rep_process(user, computer)
    else:
        while sum(computer) < 17:
            computer.append(random.randint(2,11))
            
        print(f"""your final hand {user}, your final score : {sum(user)}
computer's final hand {computer}, computer final score : {sum(computer)}""")
        
        result(user, computer)

def result(user, computer):
    if sum(computer) <= 21:
        if sum(user) > sum(computer):
            print(f"Congrats you has greater hands than computer.\n{game_logo[1]}\n\n")
        elif sum(user) == sum(computer):
            print(f"Computer and You has equal hands.\nGame is draw.\n\n")
        else:
            print(f"Sorry computer has greater hands than you.\n{game_logo[2]}\n\n")
    elif sum(user) == sum(computer):
        print("Computer and You has equal hands.\nGame is draw.\n\n")
    else:
        print(f"Computer went over.\n{game_logo[1]}\n\n")
    rep_process(user, computer)

def rep_process(user, computer):
    if input("Do you want to play again? (y/n) : ") == "y":
        new_game(user, computer)
    else:
        print("*****Thankyou*****")    

user = []
computer = []
new_game(user, computer)