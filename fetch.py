import add

# functions to fetch all kind of data

# fetch all
def fetch_all():
    add.connect.execute("SELECT * FROM VPN")
    fetch = add.connect.fetchall()
    print('Start fetching........')
    for i in fetch:
        print('------------------------------------------------------------------')
        print('Username   IP_address    Public_key                  Private_key  |')
        print('                                                                  |')
        print('------------------------------------------------------------------')
        print(i)
        add.time.sleep(0.2)
    print('\nDone Done Done !!')

# fetch username
def fetch_username():
    add.connect.execute("SELECT user_vpn FROM VPN")
    fetch = add.connect.fetchall()
    print('Start fetching........')
    for i in fetch:
        print('----------')
        print('Username:')
        print(i)
        add.time.sleep(0.2)
    print('\nDone Done Done !!')

# fetch ips
def fetch_IP():
    add.connect.execute("SELECT user_ips FROM VPN")
    fetch = add.connect.fetchall()
    print('Start fetching........')
    for i in fetch:
        print('------------')
        print('IP_address: |')
        print('------------')
        print(i)
        add.time.sleep(0.2)
    print('\nDone Done Done !!')

# fetch Public keys

def fetch_public_key():
    add.connect.execute("SELECT public_key FROM VPN")
    fetch = add.connect.fetchall()
    print('Start fetching........')
    for i in fetch:
        print('-------------------------------------------------------------')
        print(i)
        add.time.sleep(0.2)
    print('\nDone Done Done !!\n')
# fetch Private keys
def fetch_private_key():
    add.connect.execute("SELECT private_key FROM VPN")
    fetch = add.connect.fetchall()
    print('Start fetching........')
    for i in fetch:
        print('-------------------------------------------------------------')
        print(i)
        add.time.sleep(0.2)
    print('\nDone Done Done !!\n')

# fetch username and ip
def user_ip():
    add.connect.execute("SELECT user_vpn FROM VPN")
    fetch_user = add.connect.fetchall()
    add.connect.execute("SELECT user_ips FROM VPN")
    fetch_ips = add.connect.fetchall()
    for user in fetch_user:
        for ip in fetch_ips:
            print('--------')
            print('User-Name:',''.join(user))
            print('User-IP:',''.join(ip))
            add.time.sleep(0.2)
user_ip()