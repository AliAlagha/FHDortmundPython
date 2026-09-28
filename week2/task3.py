if __name__ == '__main__':
    cars = [{'make': ' Google ', 'model': 216, 'color': 'Black'},
            {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
            {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    print("Original list of dictionaries:", cars)
    result = sorted(cars, key=lambda x: int(x['model']), reverse=True)
    print("Sorting the list of dictionaries:", result)
