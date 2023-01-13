import add



#infrastructure
#menu class
#class for searching in db with RowID
#class for searching anything by expacting word

class Searching_Row():
    # initializing
    def __init__(self):
        #logo
        add.clean()
        add.art.creator()
        #user Seaching_menu 
        print("""Searching Menu\n
        \n>.1 Searching by ID\n>.2 Searching by anything by Column\n>.3 Exit""")
        self.dec_user = int(input('Choose: '))
        self.dec_user == 1 and self.user_search()
        self.dec_user == 2 and self.search_any()
        self.dec_user == 3 and exit()
  


    


    #to search inside column    
    def inside_column(self):
        print('Search inside Which Column: ')
        print("""
        Columns Names:
        >.1 In Username.
        >.2 In User IP.
        >.3 In Public_Key.
        >.4 In Private_key.
        """
        )
        # input in column
        self.in_col = int(input('Pick a Column: '))
        try:
            if self.in_col == 1:
                self.take = "user_vpn"
            elif self.in_col == 2:
                self.take = "user_ips"
            elif self.in_col == 3:
                self.take = "public_key"
            elif self.in_col == 4:
                self.take = "private_key"
            else:
                print('wrong input')
        except Exception:
            print('Oops Wrong input\nExting.....')
            exit()

    # by which column doing search
    def by_which_column(self):
        add.clean(),add.art.creator()
        print("""
        By Which Column you Searching By:
        
        >.1 By Username.
        >.2 By User IP.
        """
        )
        # input by column
        self.by_col = int(input('Pick a Column: '))
        try:
            if self.by_col == 1:
                print(add.colors().green,add.colors().uderline,
                """\nNote:\nSearching by username\nOR\nSearching by letters""",
                add.colors().end)
                self.pick = "user_vpn"

            elif self.by_col == 2:
                self.pick = "user_ips"
                print(add.colors().green,add.colors().uderline,
                '\nNote If you search inside any column\nby user_ip Please add subent EX: 10.10.11.1/24',
                add.colors().end)
            else:
                print('wrong input')
        except Exception:
            print('Oops Wrong input\nExting.....')
            exit()

    # Search by ID inside columns.
    def user_search(self):
        self.inside_column()
        self.id = int(input('Which ID: '))
        # call choose method
        # insert choose into db 
        self.exe = add.connect.execute(f"SELECT {self.take} FROM VPN WHERE rowid = (?)",(self.id,))
        self.loop()
    
    # searching inside db
    def loop(self):
        self.fetching = add.connect.fetchall()
        for x in self.fetching:
            print(x)
        
# Class for searching anything by expacting word or number.
class Searching_any(Searching_Row):
    def search_any(self):
        self.inside_column()
        add.clean()
        self.by_which_column()
        self.user_find_word = str(input('Seaching word: '))
        self.exe =  add.connect.execute(f"SELECT {self.take} FROM VPN WHERE {self.pick}  like (?)",('%' + self.user_find_word,))
        self.loop()


#                     b
#                       g           bug
#                       u        bug
#       bugbug          b       g
#             bug      bugbug bu
#                bug  bugbugbugbugbugbug
#   bug   bug   bugbugbugbugbugbugbugbugb
#      bug   bug bugbugbugbugbugbugbugbugbu
#    bugbugbugbu gbugbugbugbugbugbugbugbugbu
#   bugbugbugbug  
#    bugbugbugbu gbugbugbugbugbugbugbugbugbu
#      bug   bug bugbugbugbugbugbugbugbugbu
#   bug   bug  gbugbugbugbugbugbugbugbugb
#                bug  bugbugbugbugbugbug
#             bug      bugbug  bu
#       bugbug          b        g
# 	               g        c
# 			b        d
# 	========================================
# 			Created By: Bug
# 	Name:leon                    			
#     	Github: leonvita91                      
#     	Project:Generate Wireguard users & keys 
# 	========================================


