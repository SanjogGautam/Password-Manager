from cryptography .fernet import Fernet, MultiFernet
import os


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)


def load_key():
    return open("key.key", "rb").read()


if not os.path.exists("key.key"):
    write_key()
key = load_key()
fer = Fernet(key)
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, write), press q to quit? ").lower()

    if mode == "q":
        print("Exiting the Password Manager by Sanjog Gautam")
        break

    if mode == "view":
        if not os.path.exists("passwords.txt"):
            print("Create a new passwords.txt folder: ")
            continue
        with open("passwords.txt", "r") as f:
            for i in f.readlines():
                username, password = i.split("|")
                print(f"Username: {username} | password= {password}")
    elif mode == "write":
        if not os.path.exists("passwords.txt"):
            print("New Password file: ")
            username = input("Enter username= ")
            password = input("Enter password= ")
            with open("password.txt", "w") as f:
                f.write(f"{username}|{password}\n")

        username = input("Enter username= ")
        password = input("Enter password= ")
        with open("passwords.txt", "a") as f:
            f.write(f"{username}|{password}\n")

    else:
        print("Invalid mode.")
        continue
