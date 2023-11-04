# @see https://docs.python.org/3/library/sqlite3.html

import sqlite3

# connection = sqlite3.connect("example.db") # creates the file
connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

cursor.execute("CREATE TABLE tasks (text, is_done)")

tasks = [
  ('Learn Python', True),
  ('Look for a job', False),
  ('Forget everything', False)
]

cursor.executemany("INSERT INTO tasks VALUES (?, ?)", tasks)

cursor.execute("""
  SELECT *
  FROM tasks
  WHERE is_done = ?
""", (True,))

for row in cursor:
  print(f'title: {row[0]}, is_done: {row[1]}')

cursor.execute("""
  SELECT *
  FROM tasks
  WHERE is_done = :is_done
""", {'is_done': True})

for (title, is_done) in cursor:
  # title = row[0]
  # is_done = row[1]
  print(f'title: {title}, is_done: {is_done}')

connection.close()
