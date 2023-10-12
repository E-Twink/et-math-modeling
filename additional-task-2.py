import utils

def main():
    a = int(input("Enter the length of the first segment: "))
    b = int(input("Enter the length of the second segment: "))
    c = int(input("Enter the length of the third segment: "))
    
    if (a < b + c) and (b < a + c) and (c < a + b):
        print(f"A triangle with sides {a}, {b}, {c} exists.")

        if a == b and b == c:
            print(f"A triangle with sides {a}, {b}, {c} is equilateral.")
        elif a == b or b == c or c == a:
            print(f"A triangle with sides {a}, {b}, {c} is isosceles.")
        else:
            print(f"A triangle with sides {a}, {b}, {c} is versatile.")
    else:
        print(f"A triangle with sides {a}, {b}, {c} not exists.")

if __name__ == "__main__":
    main()