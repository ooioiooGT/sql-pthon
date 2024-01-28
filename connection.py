import mysql.connector as myc 
from config import database_config

server = database_config['server']
port = database_config['port']
database = database_config['database']
username = database_config['username']
password = database_config['password']

# Establishing a connection to the MySQL Server
cnxn = myc.connect(
    host=server,
    port=port,
    database=database,
    user=username,
    password=password
)

cursor = cnxn.cursor()
# Example SELECT query
# query = "SELECT * FROM driver_table;"

# Execute the query
cursor.execute("SELECT * FROM driver_table;")

# Fetch all rows
rows = cursor.fetchall()
if rows:
    # Print the colum name
    column_names = [column[0] for column in cursor.description]
    print("Column Names:", column_names)
    # Print the retrieved data
    for row in rows:
        
        print(row)
else:
    column_names = [column[0] for column in cursor.description]
    print("Column Names:", column_names)
    print("No data")

# insertquery = " insert into driver_table ( Driver_id, first_name, last_name, phone_number ) value (%s ,%s ,%s ,%s)"
# value = (1, 'gilber' , 'chen', 2086038613)
# cursor.execute(insertquery,value)
# cnxn.commit()
# print("addeed ")