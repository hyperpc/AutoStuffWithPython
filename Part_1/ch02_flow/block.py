print('Plz input your name:')
name = input()
if name == 'Mary':
    print('Hello Mary')
    print('Plz input your password:')
    password = input()
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
else:
    print('Wrong name.')