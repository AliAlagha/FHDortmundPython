if __name__ == '__main__':
    words = ["red", "green", "blue", "yellow"]
    print("List of strings:", words)
    result = list(map(list, words))
    print("List of lists:", result)
