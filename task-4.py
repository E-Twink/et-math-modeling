import utils

def main():
    number = int(input("Enter the number of numbers: "))
    
    a_0 = 1
    a_1 = 1

    for i in range(number):
        print(a_0, end='')

        t = a_1
        a_1 = a_0 + a_1
        a_0 = t

        if i != number - 1:
            print(", ", end='')
    
    print()

if __name__ == "__main__":
    main()