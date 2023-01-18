import hashlib
import json


def check_password(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    if len(password) >= 8:
        for char in password:
            if char.islower():
                has_lowercase = True
            if char.isupper():
                has_uppercase = True
            if char.isdigit():
                has_digit = True
            if char in "~`!@#$%^&*()-_+={}[]|:;<>,.?":
                has_special = True
        if has_uppercase and has_lowercase and has_digit and has_special:
            return True
    return False


while True:
    print("If you want to add a password press 1:")
    print("If you want to show current saved password press 2:")
    print("If you want to exit program press 3:")
    choice = input("Choose: ")

    if choice == '1':
        password = input("Choose a Password : ")
        if check_password(password):
            print("Password Allowed")
            break
        else:
            print("Invalid password. It must contain at least 8 characters, one lowercase letter, one uppercase letter, one number and one special character (~,`,!,@,#,$,%,^,&,*,(,),-,_,+,=,{,},[,],|,:,;,<,>,,,.,?,")
    elif choice == '2':
        print("Passwords : ")
        with open("passwords.json", "r") as file:
            data = json.load(file)
            print(data)
        exit()
    elif choice == '3':
        exit()
    else:
        print("IMPUT ERROR")


password_hash = hashlib.sha256(password.encode()).hexdigest()

try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
except:
    passwords = {}

if password_hash in passwords:
    print("Password already saved")
else:
    passwords[password_hash] = password

with open("passwords.json", "w") as file:
    json.dump(passwords, file)

print("Passwords : ")
for key, value in passwords.items():
    print(key + " : " + value)

"""
Ici dans le json le mot de passe hashé est associé à son mot de pas en clair, ce qui n'a pas vraiment de sens d'un point de
vue sécuriter, mais j'ai fait cela pour une clarté de correction.
"""