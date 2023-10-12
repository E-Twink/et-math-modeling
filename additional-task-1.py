import utils

def main():
    a = int(input("Enter the coefficient \'a\': "))
    b = int(input("Enter the coefficient \'b\': "))
    c = int(input("Enter the coefficient \'c\': "))
    D = utils.discriminant(a, b, c)

    print(f"The discriminant is equal to {D}.")
    
    s = 0
    
    if D == 0:
        s = 1
    elif D > 0:
        s = 2

    if s != 0:
        print(f"This means that the equation has {s} solutions. Solutions:")
        utils.solveQuadraticEquation(a, b, c)

if __name__ == "__main__":
    main()