if __name__ == '__main__':
    number = 5
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of " + str(number) + " = " + str(factorial))

    whole = 7
    decimal = 9.8
    big = 42
    digits = "123"
    zero = 0

    print("int to float:", float(whole))
    print("float to int:", int(decimal))
    print("int to string:", str(big))
    print("string to int:", int(digits))
    print("int to bool (0):", bool(zero))
    print("int to bool (7):", bool(whole))

