import sys
import os

def clear():
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win"):
        os.system("cls")

def discriminant(a, b, c):
    return ((b**2) - (4*a*c))

def solveQuadraticEquation(a, b, c):
    if discriminant(a, b, c) > 0:
        print(f"x_0 = {(-b-(discriminant(a, b, c)**(1/2)))/(2*a)}")
        print(f"x_1 = {(-b+(discriminant(a, b, c)**(1/2)))/(2*a)}")
    elif discriminant(a, b, c) == 0:
        print(f"x = {(-b-(discriminant(a, b, c)**(1/2)))/(2*a)}")

class color:
    RESET = "\033[0m"
    ERROR = "\033[91m"