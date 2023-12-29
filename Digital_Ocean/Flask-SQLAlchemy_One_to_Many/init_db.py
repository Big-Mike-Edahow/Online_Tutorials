# init_db.py

import sqlite3

conn = sqlite3.connect('database.db')
curs = conn.cursor()

with open('schema.sql') as f:
    conn.executescript(f.read())

title = "Favorite Music"
content = "From hair metal bands to pop music to instrumental, my music tastes vary depending on my mood."

data_tuple = (title, content)
sql_query = '''INSERT INTO post (title, content) VALUES (?, ?);'''

curs.execute(sql_query, data_tuple)
conn.commit()

title = "Burger Joints"
content = "The french fries at burger joints can really vary. Freddy's has long, skinny fries. Arby's has curly fries."

data_tuple = (title, content)
sql_query = '''INSERT INTO post (title, content) VALUES (?, ?);'''

curs.execute(sql_query, data_tuple)
conn.commit()

conn.close()

