import sqlite3
import subprocess
from time import sleep
from datetime import datetime
# import My Code
import add,fetch,delete
import search as find

#Exting handle
try:    
    # create and check function
    def create():
        add.clean()
        add.art.creator()
        add.art.section()
        print('>.1 Create new user.\n>.2 Check exsiting username & IP\n>.3 menu\n>.4 Exit')
        try:
            dec = int(input('Choose one of the Options: '))
            if dec == 1:
                add.Vpn_input()
                add.check_username()
                add.check_ip()
                add.insert_data()
                print("Username && IP With keys >> has been created.")
                sleep(0.5)
                print('Would you like to add another user ??')
                another = str(input('/y|n/ : '))
                another = 'y' and create()
                another = 'n' and print('Back to menu.....')
            elif dec == 2:
                add.Vpn_input()
                add.check_username()
                add.check_ip()
                add.art.not_exis()
            elif dec == 3:
                menus()
            elif dec == 4:
                exit()
            add.art.done()
            menus()
            sleep(1)
        except Exception:
            print('Bad input try one of numbers above !!')
            sleep(2)
            menus()

    def call():
        add.clean()
        add.art.creator()
        add.art.fech_art()
        print('>.1 Fetch ALL.\n>.2 Fetch username\n>.3 Fetch IPs\n>.4 Fetch Public key.\n>.5 Fetch Private key.\n>.6 Fetch Users & IPs.\n>.7 Fetch username & IPs & Public key.')
        dec = int(input('Choose one of the Options: '))
        dec == 1 and fetch.fetch_all()
        dec == 2 and fetch.fetch_username()
        dec == 3 and fetch.fetch_IP()
        dec == 4 and fetch.fetch_public_key()
        dec == 5 and fetch.fetch_private_key()
        dec == 6 and fetch.fetch_user_and_ip()
        dec == 7 and fetch.fetch_user_ip_public_key()
    
    def remove():
        pass
    
    def menus():
        add.clean()
        add.art.creator()
        print('What Would You Like To Do ?')
        print('>.1 Create new user.\n>.2 Fetch Info\n>.3 Delete Info\n>.4 Search Info\n>.5 Exit')
        # user decision:
        dec = int(input('Choose one of the Options: '))
        dec == 1 and create()
        dec == 2 and call()
        dec == 3 and remove()
        dec == 4 and find.Searching()
        dec == 5 and print('Good Bye....') , exit()
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