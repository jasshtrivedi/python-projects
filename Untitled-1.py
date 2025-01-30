import os
import math
import time

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
#-----------------------------------------------------------------
#-Storage---
num1 = 0
num2 = 0
#-----------------------------------------------------------------------------

def Numbers():
    global num1, num2
    num1 = float(input("Enter the first number."))
    time.sleep(0.2)
    num2 = float(input("Enter the second number."))
    if num2 == "0.0":
        print("WARNING!, Number may not be divisible by 0")
    Operation()
    

def Restart():
    Retry = input("Do you want to restart?")
    if Retry == "y":
        clear_terminal()
        CalculatorEntry()
    else:
        print("Okay.")
        clear_terminal()

def Operation():
    functions = input("Enter calculation here: (+,-,/,*) or Q to quit")
    if functions == "Q":
        clear_terminal()
        print("Resetting.")
        time.sleep(2)
    elif functions == "+":
        print(num1 + num2)
        Restart()
    elif functions == "-":
        print(num1 - num2)
        Restart()
    elif functions == "*":
        print(num1 * num2)
        Restart()
    elif functions == "/":
        print(num1 / num2)
        Restart()
    else:
        print("invalid function")
        clear_terminal()    



def CalculatorEntry():
    Question = input("Do you want to calculate?")
    if Question == "Yes":
        print("Okay.")
        Numbers()

CalculatorEntry()