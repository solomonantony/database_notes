# use sqlite3 package
import sqlite3
folder_name = '.'
file_name = 'ecars.db'
connection = sqlite3.connect(folder_name +'/' + file_name)
my_cursor = connection.cursor()
#Viewing the tables in the database
my_cursor.execute('select * from sales')
rows = my_cursor.fetchall()
print(rows)
for row in rows:
  print(row)
#==  Viewing the column names of a table
#using cursor.description
column_names = [desc[0] for desc in my_cursor.description]
print(column_names)
#
#using the rows  of sqlite_schema table
my_cursor.execute('select * from sqlite_schema')
rows = my_cursor.fetchall()
for row in rows:
  print(row[4])
