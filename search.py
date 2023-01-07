import add

class Searching():
    def __init__(self):
        self.id = int(input('ID Row searching: '))
        self.take = add.connect.execute(f"SELECT user_vpn FROM VPN Where rowid = (?)",(self.id,))
        self.call = add.connect.fetchall()
        # self.ser = ser
        self.loop()
        self.calling()
    
    def loop(self):
        # add.connect.execute(f"SELECT rowid ,  user_vpn FROM VPN WHERE user_vpn like (?)",(self.ser,))
        for x in self.call:
            print(x)
        print('stop')
    
    def calling(self):
        self.id
        self.take
        self.call
        for s in self.call:
            print(s,'second search')
out = Searching()



