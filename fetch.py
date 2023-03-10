import add
from time import sleep

# functions to fetch all kind of data

# fetch all
def fetch_all():
    add.connect.execute("SELECT rowid FROM VPN")
    fetch_row = add.connect.fetchall()
    add.connect.execute("SELECT user_vpn FROM VPN")
    fetch_user = add.connect.fetchall()
    add.connect.execute("SELECT user_ips FROM VPN")
    fetch_ip = add.connect.fetchall()
    add.connect.execute("SELECT public_key FROM VPN")
    fetch_pub_key = add.connect.fetchall()
    add.connect.execute("SELECT private_key FROM VPN")
    fetch_priv_key = add.connect.fetchall()
    add.connect.execute("SELECT date FROM VPN")
    fetch_date = add.connect.fetchall()
    add.connect.execute("SELECT time FROM VPN")
    fetch_time = add.connect.fetchall()
    print('Start fetching........\n'
            '---------------------')
    for row,user,ip,pub,priv,date,time in zip(fetch_row,
    fetch_user,
    fetch_ip,
    fetch_pub_key,
    fetch_priv_key,
    fetch_date,
    fetch_time):

        print('----------------------------------------------------------------------------------------------')
        print('RowID:',row ,'\n',
        'Username: ' + ''.join(user) + '\n',
        'Ip_Adress: ' + ''.join(ip) + '\n',
        ''.join(pub) + '\n',
        ''.join(priv) + '\n',
        ''.join(date) + '\n',
        ''.join(time)) 
        sleep(0.2)
    print('------------------------------------------------------------------')
    print('\nDone Done Done !!')


# fetch username
def fetch_username():
    add.connect.execute("SELECT rowid, user_vpn FROM VPN")
    fetch = add.connect.fetchall()
    print('Start fetching........\n'
          '------------------')
    for x in fetch:
        print('----------')
        print('RowID:',x)
        sleep(0.2)
    print('\nDone Done Done !!')

# fetch ips
def fetch_IP():
    add.connect.execute("SELECT user_ips FROM VPN")
    fetch = add.connect.fetchall()
    add.connect.execute("SELECT rowid FROM VPN")
    fetch_row = add.connect.fetchall()
    print('Start fetching........\n'
          '------------------')
    for x,y in zip(fetch_row,fetch):
            print('RowID:',x,''.join(y))
            sleep(0.2)
    print('------------')
    print('\nDone Done Done !!')

# fetch Public keys
def fetch_public_key():
    add.connect.execute("SELECT rowid FROM VPN")
    fetch_row = add.connect.fetchall()
    add.connect.execute("SELECT public_key FROM VPN")
    fetch = add.connect.fetchall()
    print('Start fetching........\n'
          '------------------')
    for x , y in zip(fetch_row , fetch):
        print('-------------------------------------------------------------')
        print('RowID:',x,''.join(y))
        sleep(0.2)
    print('\nDone Done Done !!\n')
# fetch Private keys
def fetch_private_key():
    add.connect.execute("SELECT rowid FROM VPN")
    fetch_row = add.connect.fetchall()
    add.connect.execute("SELECT private_key FROM VPN")
    fetch = add.connect.fetchall()
    print('Start fetching........\n'
          '------------------')
    for x , y in zip(fetch_row , fetch):
        print('-------------------------------------------------------------')
        print('RowID:',x,''.join(y))
        sleep(0.2)
    print('\nDone Done Done !!\n')

# fetch username and ip
def fetch_user_and_ip():
    add.connect.execute("SELECT rowid FROM VPN")
    fetch_row = add.connect.fetchall()
    add.connect.execute("SELECT user_vpn , user_ips FROM VPN")
    fetch = add.connect.fetchall()
    for x , y in zip(fetch_row,fetch):
        print('--------')
        print('RowID:',x,' || '.join(y))
        sleep(0.2)
    print('--------')
    print('\nDone Done Done !!\n')
# fetch username & IP & public key
def fetch_user_ip_public_key():
    add.connect.execute("SELECT rowid FROM VPN")
    fetch_row = add.connect.fetchall()
    add.connect.execute("SELECT user_vpn , user_ips , public_key FROM VPN")
    fetch = add.connect.fetchall()
    print('fetching......')
    for x , y in zip(fetch_row, fetch):
        print('---------------------------------------------------------------------------------')
        print('RowID:',x,' ||   '.join(y))
        sleep(0.1)
    print('------------------------------------------------------------------------------------')
    print('\nDone Done Done !!\n')


# call functions for test 
# fetch_all()
# fetch_IP()
# fetch_public_key()
# fetch_private_key()
# fetch_user_and_ip()
# fetch_user_ip_public_key()