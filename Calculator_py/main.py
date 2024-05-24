import os
from logo import calc_logo

def start_calc(num1, num2, res):
    os.system("cls")
    print(f"{calc_logo}\n\n")
    num1 = float(input("Enter the first number: "))
    res = num1
    calc(num1, num2, res)

def calc(num1,num2, res):
    oper = ["+", "-", "*", "/"]
    operator = input("Enter the operator from the below option:\n[ + , - , * , / ]\n")
    if operator in oper:
        num2 = float(input("Enter the next number: "))
        print(f"{res} {operator} {num2} =", end = " ")
        if operator == "+":
            res += num2
        elif operator == "-":
            res -= num2
        elif operator == "*":
            res *= num2
        else:
            res /= num2
        print(f"{res}")
    else:
        print("You have entered an wrong operator, please try again!!!")
        calc(num1, num2, res)
    rep_process(num1, num2, res)

def rep_process(num1, num2, res):
    rep = input("Type 'y' to continue in this same calculation.\nType 'n' to start a new calculation.\nType 'end' to end the entire calculation.\n")
    os.system("cls")
    print(calc_logo)
    if rep == "y":
        calc(num1, num2, res)
    elif rep == "n":
        start_calc(num1, num2, res)
    elif rep == "end":
        print("*****Thankyou for using the calculator app*****")
    else:
        print("Please enter an correct input.")
        rep_process(num1, num2, res)

num1 = num2 = res = 0
start_calc(num1, num2, res)