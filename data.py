import sqlite3
import subprocess
from datetime import datetime 

# add color to texts.
class colors:
    pink = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    uderline = '\033[4m'

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

# user input username & ip.
def Vpn_input():
    #define global var
    global user_name,user_ips,user_public_key,user_private_key,date,time
    #Generate keys
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
    #variables stores keys,date,time
    user_public_key = public
    user_private_key = private
    date = dates
    time = times
    #User_name_input & user_input ip
    user_name = input(str("Insert username: ")) #15
    user_ips = input(str("Insert IP:"))# 20
    # add the lenght inside list.
    username_len_input = len(user_name)
    userip_len_input = len(user_ips)
    #check if the username & ip are not out of range.
    while username_len_input > 10 or userip_len_input > 15:
        print(colors.bold,colors.red,'WARNING!!',colors.end)
        print('You have entered:')
        print('Username_Charactor=',username_len_input,'IP_length=',userip_len_input)
        print(colors.bold,colors.cyan,'\nUSER_NAME 10 CHARACTOR MAX && IPs 15 DIGIT MAX.',colors.end)
        #User_name_input & user_input ip
        user_name = input(str("Insert username: ")) #15
        user_ips = input(str("Insert IP:")) #20
        # add the lenght inside list.
        username_len_input = len(user_name)
        userip_len_input = len(user_ips)
    # end function.

def add_ips():
    #insert the values to VPN TABLE
    connect.execute("INSERT INTO VPN VALUES (?,?,?,?,?,?)",
    (
    (user_name),
    (user_ips + "/24"),
    ('Public_key= ' + user_public_key.replace('\n', '')), #replace char \n to normal key
    ('Private_key' + user_private_key.replace('\n', '')), #replace char \n to normal key
    ('Date: ' + date),
    ('Time: ' + time)
    ))
    create.commit() #Commit into db
    subprocess.run("rm privatekey.txt publickey.txt",shell=True) #delete the keys
#end function.

def checking():
    connect.execute("SELECT user_vpn FROM VPN")
    search = connect.fetchall()
    for searchs in search:
        user = "".join(searchs) # convert from tuple to string
        if user == user_name:
            print('name exsit')
            Vpn_input() #if the name exist it will return to Vpn_input function again.
            checking() # checking again
        else:
            print('done')
            break

        
#add users & ips & keys & date & time into Database
    
    
#Call functions
Vpn_input() # call input function
checking() # call checking function
add_ips() # call add to database function




#-----------------------------------------------------


#Close the db after finishing
#create.close()
    #Notes:
    #if you want to search something in specific table and column
    #connect.execute("SELECT * FROM VPN WHERE user_vpn == (?)",(user_name,))