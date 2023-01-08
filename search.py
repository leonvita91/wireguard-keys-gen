import add

class Searching():
    # initializing
    def __init__(self):
        #logo
        add.clean()
        add.art.creator()
        #call search by ID method
        self.user_search()
    
    # Search by ID inside columns.
    def user_search(self):
        print('Search by Column & ID')
        print("""
        Columns Names:
        >.1 user_vpn
        >.2 user_ips
        >.3 public_key
        >.4 private_key
        """
        )
        try:
            self.row = int(input('Which Column: '))
            if self.row == 1:
                self.take = "user_vpn"
            elif self.row == 2:
                self.take = "user_ips"
            elif self.row == 3:
                self.take = "public_key"
            elif self.row == 4:
                self.take = "private_key"
            else:
                print('wrong input')
            self.id = int(input('Which ID: '))
            self.exe = add.connect.execute(f"SELECT {self.take} FROM VPN WHERE rowid = (?)",(self.id,))
            self.fetching = add.connect.fetchall()
            self.loop()
        except Exception:
            print('Oops Wrong input\nExting.....')
            exit()
    
    # looping inside db
    def loop(self):
        for x in self.fetching:
            print(x)

    # searching by anything
    # To be continue xd    

test = Searching() #used only for testing


# example class with methods and object and inhert.
# class Searching():
#     def __init__(self):
#         self.id = int(input('ID Row searching: '))
#     def ser(self):
#         self.take = add.connect.execute(f"SELECT user_vpn FROM VPN Where rowid = (?)",(self.id,))
#         self.call = add.connect.fetchall()
#         # self.ser = ser
#         self.loop()
#     def loop(self):
#         # add.connect.execute("SELECT rowid ,  user_vpn FROM VPN WHERE user_vpn like (?)",(self.ser,))
#         for x in self.call:
#             print(x)
#         print('stop')
    
# class Searching2(Searching):
#     def __init__(self):
#         super().__init__()
#         super().ser()
#         self.id = int(input('second input'))
#         self.ser()
# out1 = Searching2()

# add.connect.execute("SELECT rowid, user_vpn FROM VPN")
# t = add.connect.fetchall()
# for x in t:
#     print(x)



