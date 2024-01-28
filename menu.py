import mysql.connector as myc
from config import database_config
import pandas as pd 
from datetime import datetime
server = database_config['server']
port = database_config['port']
database = database_config['database']
username = database_config['username']
password = database_config['password']

try: 

    cnxn = myc.connect(
    host=server,
    port=port,
    database=database,
    user=username,
    password=password
    )
    if cnxn.is_connected():
        cursor =  cnxn.cursor()
        db_Info = cnxn.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        

except myc.Error as e:
    print("Error while connecting to MySQL", e)




# Menu list 
choice = None
while choice != "5":
    print ("1. display the user table")
    print ("2. add the user to the table")
    print ("3. update the user information")
    print ("4. delet the user")
    print ("5. Quit")

    choice = input("> ")
    
    if choice == "1" :
        cursor.execute("SELECT * FROM User ")
        rows = cursor.fetchall()
        if rows:
            custom_column_names = ['ID','First name','Last name','last update']
            pf = pd.DataFrame(rows)
            pf.columns = custom_column_names
            print (pf)
        else:
            print("no data ")
    elif choice == "2" : 
        
        cursor.execute("INSERT INTO User (last_name, first_name, birthday, gender)VALUES ('Chen', 'Gilber','1998-10-02', 'Male')")
        print ('add actor sucessfully')
    
    elif choice == "3" : 
        print (' update actor sucessfully')
    elif choice == "4" : 
        print ('delete sucessfuly')

