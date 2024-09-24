import os
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    file = open('key.txt', 'wb')
    file.write(key)
    file.close()


if not os.path.isfile('key.txt'):
    write_key()


def load_key():
    file = open('key.txt', 'rb')
    key: bytes = file.read()
    file.close()
    return key


password = input('Enter your master password: ')

key = load_key() + password.encode()
fernet = Fernet(key)


def view():
    file = open('passwords.txt', 'r')
    for line in file.readlines():
        # removes the extra line at the end of the file
        data = line.rstrip()
        # Skip empty lines
        if not data:
            continue
        # splits the username and the password
        user, passw = data.split(':')
        print("Username: ", user, ",", " Password: ",
              fernet.decrypt(passw.encode()).decode())
    file.close()


def add():
    unm = input('Enter your username: ')
    pwd = input('Enter your password: ')

    file = open('passwords.txt', 'a')
    file.write(unm + ":" + fernet.encrypt(pwd.encode()).decode() + "\n")
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
