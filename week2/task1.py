def last(t):
    return t[-1]


if __name__ == '__main__':
    L = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print("Sample list:", L)
    print("Sorted by last element:", sorted(L, key=last))
