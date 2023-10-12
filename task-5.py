import utils

def main():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    
    print(f"Еhe quotient of dividing the first number by the second number: {number_1 // number_2}.")
    if number_1 % number_2 == 0:
        print("The first number is divided without remainder by the second number.")
    else:
        print(f"The remainder of the division of the first number by the second: {number_1 % number_2}.")

if __name__ == "__main__":
    main()