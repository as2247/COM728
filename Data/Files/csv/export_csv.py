def export(file_path, bots_to_export):
    print("Exporting...")
    with open(file_path, "a") as file:
        for values in range(bots_to_export):
            bot_id = input("Enter Bot ID")
            bot_name = input("Enter Bot Name")
            bot_paint = input("Enter Bot Paint")
            file.write(f"\n{bot_id},{bot_name},{bot_paint}")
    print("Done!")


def run():
    export("./exported_bots.csv", 2)


if __name__ == "__main__":
    run()
