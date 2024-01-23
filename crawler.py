import sqlite3
from get_data import sort_data


con = sqlite3.connect("database.db")

cur = con.cursor()

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
