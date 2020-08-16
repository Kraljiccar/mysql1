import os
import pymysql

# (modify this variable if running on another environment)
username = os.getenv('USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        list_of_names = ['FRED', 'FRED']
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)
        connection.commit()
finally:
    connection.close()