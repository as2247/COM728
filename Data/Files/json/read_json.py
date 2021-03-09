import json

def read(file_path):
    with open(file_path) as file:
        data = json.load(file)
        city_name = data["city"]
        population = data["population"]
        print(f"City Name: {city_name}")
        print(f"Population: {population}")

        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")

def run():
    read("robocity.json")

run()