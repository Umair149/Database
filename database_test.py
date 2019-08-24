import sqlite3

conn = sqlite3.connect('first.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS  JobStuff(job_id REAL, salery REAL, value REAL)')

def data_entry():
    c.execute("INSERT INTO JobStuff VALUES(01, 25000, 05 )")
    conn.commit()


def read_db():
    c.execute('SELECT * from JobStuff')
    data = c.fetchall()
    print (data)

create_table()
data_entry()
read_db()
c.close()
conn.close()