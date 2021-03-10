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

def run():
    load_data("./titanic.csv")
    num_records = len(records)
    print(f"Successfully Loaded {num_records} records")


if __name__ == "__main__":
    run()