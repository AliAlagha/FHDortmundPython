if __name__ == '__main__':
    n = int(input("Type a number: "))
    if n < 0:
        print("There is no factorial for negative numbers")
    else:
        result = 1
        counter = 2
        while counter <= n:
            result *= counter
            counter += 1
        print("The factorial of " + str(n) + " is " + str(result))

