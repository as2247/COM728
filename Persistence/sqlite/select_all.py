import sqlite3


def retrieve_bots():
    db = sqlite3.connect("bots.db")
    sql = "SELECT * FROM bots"

    cursor = db.cursor()
    cursor.execute(sql)

    bot_name = cursor.fetchall()
    db.close()

    for name in bot_name:
        print(name)


def run():
    retrieve_bots()


if __name__ == "__main__":
    run()