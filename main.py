password = input('Enter your master password: ')


def view():
    file = open('passwords.txt', 'r')
    for line in file.readlines():
        #removes the extra line at the end of the file
        data = line.rstrip()
        # Skip empty lines
        if not data:
            continue
        #splits the username and the password
        user, passw = data.split(':')
        print("Username: ", user, ",", " Password: ", passw)
    file.close()


def add():
    unm = input('Enter your username: ')
    pwd = input('Enter your password: ')

    file = open('passwords.txt', 'a')
    file.write(unm + ":" + pwd + "\n")
    file.close()


while True:
    mode = input('View passwords or add a new one (view/add): ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid input')
        continue
