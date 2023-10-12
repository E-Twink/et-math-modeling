import utils

def main():
    n = int(input("Enter a number: "))
    
    for i in range(2, n):
        if i != 2:
            print(", ", end='')

        d = [1]
        for j in range(2, int(i/2)):
            if i % j == 0:
                d.append(j)
        s = 0
        for j in d:
            s += j
        if i == s:
            print(f"{i}", end='')
    
    print()

if __name__ == "__main__":
    main()