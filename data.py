import sqlite3
import subprocess
from datetime import datetime 

#initialize database
create = sqlite3.connect("database.db")
connect = create.cursor()

#Create TABLE only IF NOT Exist
connect.execute("""CREATE TABLE IF NOT EXISTS VPN (
      user_vpn text,
      user_ips text,
      public_key text,
      private_key blob,
      date blob,
      time blob
      )""")

def user_input():
    #read keys 
    subprocess.run("wg genkey | tee privatekey | wg pubkey > publickey",
    shell=True,capture_output=True
    )
    #convert keys to txt file
    subprocess.run("mv publickey publickey.txt && mv privatekey privatekey.txt",shell=True)
    #format date and time
    now = datetime.now()
    dates = now.strftime("%Y-%m-%d")
    times = now.strftime("%H:%M:%S")
    #read keys file
    with open("publickey.txt","r") as pk:
        public = pk.read()
    with open("privatekey.txt","r") as prk:
        private = prk.read()
    # user input
    user_name = input(str("Insert username: "))
    user_ips = input(str("Insert IP:"))
    user_public_key = public
    user_private_key = private
    date = dates
    time = times 
    # reverse function
    add_ips(
    user_name,
    user_ips,
    user_public_key,
    user_private_key,
    date,
    time
    )
#add users & ips & keys & date & time into db
def add_ips(
    user_name,
    user_ips,
    user_public_key,
    user_private_key,
    date,
    time
    ):
    #insert values to VPN TABLE
    connect.execute("INSERT INTO VPN VALUES (?,?,?,?,?,?)",
    (
    (user_name),
    (user_ips + "/24"),
    ('Public_key= ' + user_public_key.replace('\n', '')), #replace char \n to normal key
    ('Private_key' + user_private_key.replace('\n', '')), #replace char \n to normal key
    ('Date: ' + date),
    ('Time: ' + time)
    ))

    #Commit into db
    create.commit()
    #delete the keys
    subprocess.run("rm privatekey.txt publickey.txt",shell=True)
    
    #should deltet after finish
    connect.execute("SELECT rowid, * FROM VPN") #search
    items = connect.fetchall()
    for item in items:
         print(item)

#-----------------------------------------------------

# #Checking if the ip exsit
# def checking():
#     #read db with row id
#     connect.execute("SELECT rowid, * FROM VPN") #to check with rowid use WHERE rowid = 1
#     items = connect.fetchall()
#     for item in items:
#         print(item[3])
#     userinput = '10.10.11.1'
#     items = connect.fetchall()
#     for item in items:
#         item_list = [item[2]]
#     print(item_list)
#     if item_list == userinput:
#         print('ip exist')
#         break
#     else:
#         print('new ip')
#         break

# #call fucn
user_input()
# checking()

#Close the db after finishing
create.close()