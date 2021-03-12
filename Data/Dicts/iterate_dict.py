def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences


def display_keys(data):
    print("Keys:")
    for key in data.keys():
        print(key)


def display_values(data):
    print("\nValues:")
    for value in data.values():
        print(f"{value}")


def display_items(data):
    print("\nPairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    data_list = pattern()
    display_keys(data_list)
    display_values(data_list)
    display_items(data_list)


if __name__ == "__main__":
    run()