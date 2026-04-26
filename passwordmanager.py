from cryptography .fernet import Fernet, MultiFernet
import os
import hashlib
materh_hash="b840572abb058f9d2228c9b71ca3c16744d9172a631ea7a709a32f57deceddb2"
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
master_password=input("Enter master password= ")
attempt=hashlib.sha256(master_password.encode()).hexdigest()
if materh_hash!=attempt:
    print("Access denied. Incorrect Password")
    exit()
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, write), press q to quit? ").lower()

    if mode == "q":
        print("Exiting the Password Manager by Sanjog Gautam")
        break


    if mode == "view":
        if not os.path.exists("passwords.txt"):
            print("Create a new passwords.txt file: ")
            continue
        with open("passwords.txt", "r") as f:
            for i in f.readlines():
                data=i.strip()
                username, password = data.split("|")
                d_password=fer.decrypt(password.encode()).decode()
                print(f"Username: {username} | password= {d_password}")
    elif mode == "write":
        if not os.path.exists("passwords.txt"):
            print("New Password file: ")
        username = input("Enter username= ")
        password = input("Enter password= ")
        e_password=fer.encrypt(password.encode()).decode()
        with open("passwords.txt", "a") as f:
            f.write(f"{username}|{e_password}\n")

    else:
        print("Invalid mode.")
        continue
