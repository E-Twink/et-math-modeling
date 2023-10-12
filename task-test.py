import utils

def main():
    utils.clear()

    x = 3
    
    y = (4*(x**8.5) - x**6.5) / (x**3 + 3/x) + 80 * ((27*(x**4)+12*(x**3)-5*(x**2)+10)**(1/2))
    print(f"y = {y}")
    y = ((3%2)+(16.7//4.32))/(14.5+(31%12)-int(x**3.4))
    print(f"y = {y}")

if __name__ == "__main__":
    main()