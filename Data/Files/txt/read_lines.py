def search(file_name):
    print("Searching...")
    with open("./library.txt") as file:
        for location in file:
            print(f"Looked in {location.strip()} section")
    print("...Done!")

def run():
    search("./library.txt")

if __name__ == "__main__":
    run()