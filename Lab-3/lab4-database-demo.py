#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db")
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row
#now we create a cursor to work with db
cursor = dbconnect.cursor()
#execute insert statement
cursor.execute('''INSERT INTO sensors values(1, 'door', 'kitchen')''')
cursor.execute('''INSERT INTO sensors values(2, 'temperature', 'kitchen')''')
cursor.execute('''INSERT INTO sensors values(3, 'door', 'garage')''')
cursor.execute('''INSERT INTO sensors values(4, 'motion', 'garage')''')
cursor.execute('''INSERT INTO sensors values(5, 'temperature', 'garage')''')
dbconnect.commit()
#execute simple select statement
cursor.execute('''SELECT * FROM sensors WHERE zone="kitchen"''')
#print data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] )
#execute simple select statement
cursor.execute('''SELECT * FROM sensors''')
cursor.execute('''SELECT * FROM sensors WHERE type="door"''')
#print data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] )
#close the connection
dbconnect.close()
