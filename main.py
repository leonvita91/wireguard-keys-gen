import sqlite3
import subprocess
import time
from datetime import datetime
# import My Code
import add,fetch,delete


#Exting handle
try:

#########** Call functions from add **##########
    # add.Vpn_input() 
    # add.check_username() 
    # add.check_ip() 
    # add.art.cat_done()
    # add.insert_data()


#########** Call functions from fetch **##########
    fetch.fetch_all()
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