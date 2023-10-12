import utils

def main():
    n = int(input("Enter a number: "))
    primes = [2]

    for i in range(3, n):
        t = True
        for p in primes:
            if i % p == 0:
                t = False
        if t:
            primes.append(i)
    
    while n != 1:
        for p in primes:
            if n % p == 0:
                n = n / p
                print(f"{p}", end='')
                if n != 1:
                    print(", ", end='')
    
    print()

if __name__ == "__main__":
    main()