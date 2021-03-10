import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...", end="")

    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for values in csv_reader:
            records.append(values)
    print("Done!")


def display_menu():
    print("Please select on of the following options:")
    print("[1] Display the names of all passengers")
    print("[2] Display the number of passengers that survived")
    print("[3] Display the number of passengers per gender")
    print("[4] Display the number of passengers per age group")
    selected_option = int(input())
    return selected_option


def display_passenger_names():
    print("The names of the passengers are:")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1
    print(f"{num_survived} passengers survived")


def run():
    load_data("./titanic.csv")
    num_records = len(records)
    print(f"Successfully Loaded {num_records} records\n")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    else:
        print("Error! Option is not recognised")


if __name__ == "__main__":
    run()