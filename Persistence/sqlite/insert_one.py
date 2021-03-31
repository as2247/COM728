import sqlite3


def get_bot_from_user():
    name = input("Please enter the name of the bot:")
    max_speed = input("Please enter the maximum speed of the bot:")
    max_strength = input("Please enter the maximum strength of the bot:")
    man_id = input("Please enter the manufacturer id of the bot:")
    return [name, max_speed, max_strength, man_id]


def insert_bot_in_db(data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = "INSERT INTO bots (name, max_speed, max_strength, manufacturer_id) VALUES (?,?,?,?)"
    values = [data[0], data[1], data[2], data[3]]
    cursor.execute(sql, values)
    row_id = cursor.lastrowid
    db.close()

    print(f"The last record has been added to the database")
    print(f"The last record id is: {row_id}")


def run():
    data = get_bot_from_user()
    insert_bot_in_db(data)


if __name__ == "__main__":
    run()