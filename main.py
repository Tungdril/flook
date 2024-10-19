from pyscript import display
from datetime import datetime
import pyodide_js
import asyncio

async def main():
    await pyodide_js.loadPackage("micropip")
    import micropip
    await micropip.install("sqlite3")
    import sqlite3

    now = datetime.now()
    display(now.strftime("%m/%d/%Y, %H:%M:%S"))

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

asyncio.ensure_future(main())