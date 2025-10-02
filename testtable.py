import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS colleges(
               CollegeID INTEGER PRIMARY KEY AUTOINCREMENT,
               CollegeName TEXT NOT NULL,
               DeanID INTEGER,
               FOREIGN KEY (DeanID) REFERENCES professors(ProfessorID)
                )''')

connection.commit()
connection.close()