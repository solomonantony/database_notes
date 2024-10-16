# use sqlite3 package
import sqlite3
folder_name = '.'
file_name = 'ecars.db'
connection = sqlite3.connect(folder_name +'/' + file_name)
my_cursor = connection.cursor()
query_statement = """
    Select * from sales
    where country = ? and year = ?
    """
values = ('Japan', 2017)
country_record = my_cursor.execute(query_statement, values).fetchone()
print(country_record)

