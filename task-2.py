import utils

def main():
    a_0 = int(input("Enter the first member of the progression: "))
    q = int(input("Enter the denominator of the progression: "))
    k = int(input("Enter the number of numbers in the progression: "))

    for i in range(k):
        print(a_0 * (q ** i), end='')
        if i != k - 1:
            print(", ", end='')
    
    print()
    

if __name__ == "__main__":
    main()