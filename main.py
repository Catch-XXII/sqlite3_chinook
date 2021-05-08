import sqlite3
import json

"""
if you don't want to dumps into json objects replace all json_obj with following code:

This will be replaced
json_obj = json.dumps(rows, sort_keys=True, indent=4)
    print(json_obj)

with this 
for row in rows:
    print(row)
"""


table_name = "albums"
table_names = []


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def select_from_(name, conn):
    query = f"select * from {name}"
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    columns = next(zip(*cur.description))
    for row in rows:
        row = dict(zip(columns, row))
        print(json.dumps(row, sort_keys=True, indent=4))


def get_all_table_names(conn):
    query = """SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'"""
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        beautify = str(row).strip("(',')").title()
        table_names.append(beautify)
    for i, name in enumerate(table_names):
        print(i + 1, "=>", name)
    selection = int(input("Please select one of the tables above: ")) - 1
    # check if selection between a valid range
    if selection > len(table_names) or selection < 0:
        raise Exception("index out of range")
    select_from_(table_names[selection], conn)


def select_all_albums(conn):
    query = f"select * from {table_name}"
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    json_obj = json.dumps(rows, sort_keys=True, indent=4)
    print(json_obj)


def select_with_album(_id, conn):
    query = f"select * from {table_name} where AlbumId = ?"
    cur = conn.cursor()
    cur.execute(query, (_id,))
    rows = cur.fetchall()
    json_obj = json.dumps(rows, sort_keys=True, indent=4)
    print(json_obj)


def select_with_artist(_id, conn):
    query = f"select * from {table_name} where ArtistId = ?"
    cur = conn.cursor()
    cur.execute(query, (_id,))
    rows = cur.fetchall()
    json_obj = json.dumps(rows, sort_keys=True, indent=4)
    print(json_obj)


def select_with_(title, conn):
    query = f"select * from {table_name} where title like '%{title}%'"
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    json_obj = json.dumps(rows, sort_keys=True, indent=4)
    print(json_obj)


def main():
    database = r"/Users/chinook.db"
    conn = create_connection(database)
    with conn:
        get_all_table_names(conn)
        # select_with_("Mozart", conn)
        # select_with_artist("3", conn)
        # select_with_album("3", conn)
        # select_all_albums(conn)


if __name__ == '__main__':
    main()
