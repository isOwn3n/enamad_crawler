import sqlite3
from get_data import sort_data
from write_to_csv import write_to_csv


con = sqlite3.connect("database.db")

cur = con.cursor()

cur.execute("drop table if exists buisness")

cur.execute(
    """create table
    if not exists
    buisness (id int, name text, address text, website text)
    """
)


def insert_data(data):
    """Insert data to database."""
    for i in data().values():
        cur.execute(
            "insert into buisness values (?, ?, ?, ?)", (i[0], i[2], i[3], i[1])
        )
    con.commit()


insert_data(sort_data)

text = input(
    "Writing data to database is done!\nDo you want write db's data to a csv file(Y/n)?\n#> "
)

if text.lower() == "y":
    write_to_csv()
    print("Writing data to csv file is done!")
elif text.lower() == "":
    write_to_csv()
    print("Writing data to csv file is done!")
elif text.lower() == "n":
    print("Ok!")
else:
    print("Invalid input!")
