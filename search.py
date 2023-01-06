import add

class Searching():
    def search(self ):
        add.connect.execute("SELECT rowid , user_vpn  FROM VPN WHERE public_key like '%Rc%'")
        test = add.connect.fetchall()
        for x in test:

