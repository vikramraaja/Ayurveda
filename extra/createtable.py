import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
print("connected to database successfully")

command = """CREATE T"""