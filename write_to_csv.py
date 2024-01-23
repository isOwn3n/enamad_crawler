import sqlite3
import csv


def read_database():
    """Read database."""
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("select * from buisness")
    data = cur.fetchall()
    return data

def write_to_csv():
    """Write data to csv file."""
    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "address", "website"])
        writer.writerows(read_database())

write_to_csv()
