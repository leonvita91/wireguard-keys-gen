import add 

# functions to delete data from database

def Del():
    try:
        rowid = int(input('Enter Row Number: '))
        add.connect.execute("DELETE FROM VPN  WHERE rowid = ? ",(rowid,))
        print(f'Are you sure want to del row number {rowid}:')
    except Exception:
        print('Please input numbers !!')
        Del()
    try:
        yes = 1
        no = 2
        print('=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶')
        user_del = int(input('1.Yes\n2.No\nChoose: '))
        if user_del == yes:
            add.create.commit()
            print('=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶')
            print(f'RowID:{rowid} Has been Deleted.')
        elif user_del == no:
            print(add.colors().cyan + 'Try Another Row ?: '+ add.colors().end)
            Del()
        else:
            print(add.colors().red+'Try Again !!'+add.colors().end)
            Del()
    except Exception:
        print(add.colors().red+'Wrong input please try again !! '+add.colors().end)
        Del()

