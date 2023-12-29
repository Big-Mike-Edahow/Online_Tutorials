# init_db.py

import sqlite3

conn = sqlite3.connect('database.db')
curs = conn.cursor()

with open('schema.sql') as f:
    conn.executescript(f.read())

firstname = "Steve"
lastname = "Jackson"
email = "steve@foobar.com"
age = 49
bio = '''Steve served in the United States Army at Fort Sill, Okalhoma. After that he served a Christian mission
        in France and Switzerland. Steve recieved a bachelors degree from Idaho State University.'''

data_tuple = (firstname, lastname, email, age, bio)
sql_query = '''INSERT INTO student (firstname, lastname, email, age, bio) VALUES (?, ?, ?, ?, ?);'''

curs.execute(sql_query, data_tuple)

conn.commit()
conn.close()

