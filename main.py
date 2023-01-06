import sqlite3
import subprocess
from time import sleep
from datetime import datetime
# import My Code
import add,fetch,delete


#Exting handle
try:
    subprocess.run('clear')
    add.art.creator()    
    # create and check function
    def create():
        print("""                     |=======================================================================|
                    |         This section will add new user + IP + keys :                  |
                    | Finally it will check the Username and Ip Addres if exist in Database |
                    |=======================================================================| """)
        add.Vpn_input()
        add.check_username()
        add.check_ip()
        add.insert_data()
        fetch.fetch_all()

    def call():
        pass
    def remove():
        pass
    
    def menus():
        print('What Would You Like To Do ?')
        print('>.1 Create new user.\n>.2 Fetch Info\n>.3 Delete Info')
        # user decision:
        dec = int(input('Choose one of the Options: '))
        if dec == 1:
            create()
        else:
            print('error')
    menus()









#########** Call functions from add **##########
    # add.Vpn_input() 
    # add.check_username() 
    # add.check_ip() 
    # add.art.cat_done()
    # add.insert_data()


#########** Call functions from fetch **##########
    # fetch.fetch_all()
    # fetch.fetch_IP()
    # fetch.fetch_public_key()
    # fetch.fetch_private_key()
    # fetch.fetch_user_and_ip()
    # fetch.fetch_user_ip_public_key()

    # Special case when using pandas moudle
    # test = add.create
    # data = pd.read_sql_query("SELECT user_vpn, public_key FROM VPN ", test)
    # data.to_csv('data.csv' ,index=False)

except KeyboardInterrupt:
    print('\nExsting....')
    exit()