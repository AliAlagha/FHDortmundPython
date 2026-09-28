def digit_stats(s1):
    total = 0
    count = 0
    for ch in s1:
        if ch.isdigit():
            total += int(ch)
            count += 1
    if count == 0:
        return 0, 0
    return total, total / count


if __name__ == '__main__':
    s1 = input("Enter a string: ")
    total, average = digit_stats(s1)
    print("Sum of the digits:", total)
    print("Average of the digits:", average)
