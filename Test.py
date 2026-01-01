credentials_dict = {
    'Peter Griffin': ['petergriffin@gmai.com','peter12345'],
    'Stewie Griffin': ['stewiegriffin@gmai.com','stewie12345']
}

username = input('enter user name')
password = input('enter password')

if(username in credentials_dict.keys()):
        if(password == credentials_dict[username][1]):
           print(f'{username}==>{password}')
        else:
            print('Wrong Password')
else:
    print('Wrong username')