from pyscript import display, when
import sqlite3

def main():
    print("Hello World!")
    #connection = sqlite3.connect("/databases/users.db")

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    connection.commit()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()

@when("click", "#login")
def database(event):
    print(type(event))

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
    connection.commit()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()

main()