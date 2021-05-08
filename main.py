import sqlite3

table_name = "albums"
all_table_names = []


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def generic_select(conn, name):
    query = f"select * from {name}"
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_all_albums(conn):
    query = f"select * from {table_name}"
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_with_album(conn, album_id):
    query = f"select * from {table_name} where AlbumId = ?"
    cur = conn.cursor()
    cur.execute(query, (album_id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_with_artist(conn, artist_id):
    query = f"select * from {table_name} where ArtistId = ?"
    cur = conn.cursor()
    cur.execute(query, (artist_id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_with_title(conn, title):
    query = f"select * from {table_name} where title like '%{title}%'"
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def get_all_table_names(conn):
    query = """ SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'"""
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        all_table_names.append(str(row).strip("(',')").title())
    for i, name in enumerate(all_table_names):
        print(i + 1, "=>", name)
    selection = int(input("Please select one of the tables above: ")) - 1
    generic_select(conn, all_table_names[selection])


def main():
    database = r"/Users/chinook.db"
    conn = create_connection(database)
    with conn:
        get_all_table_names(conn)


if __name__ == '__main__':
    main()
