import utils

def main():
    for i in range(9):
        for j in range(9):
            print(f"{(i+1)*(j+1):>3}", end='')
        print()

if __name__ == "__main__":
    main()