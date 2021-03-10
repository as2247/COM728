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
    print("[5] Display the number of survivors per age group")
    print("[6] Display the number of male, third-class survivors")
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


def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1
        else:
            print("Error")
    print(f"Females: {females}\nMales: {males}")


def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in records:
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"Children: {children}\nAdults: {adults}\nElderly: {elderly}")


def display_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    children_survived = 0
    adults_survived = 0
    elderly_survived = 0

    for record in records:
        survived = int(record[1])
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
                if survived == 1:
                    children_survived += 1
            elif age < 65:
                adults += 1
                if survived == 1:
                    adults_survived += 1
            else:
                elderly += 1
                if survived == 1:
                    elderly_survived += 1
    print(f"Children: {children_survived}/{children}, Adults: {adults_survived}/{adults}, Elderly: {elderly_survived}/{elderly}")


def num_male_third_class_survivors():
    survived = 0
    for record in records:
        gender = record[4]
        if gender == 'male':
            cabin_class = float(record[2])
            if cabin_class == 3:
                lived = float(record[1])
                if lived == 1:
                    survived += 1
    print(f"{survived} third class males survived")

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
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    elif selected_option == 6:
        num_male_third_class_survivors()
    else:
        print("Error! Option is not recognised")


if __name__ == "__main__":
    run()