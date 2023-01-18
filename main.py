import tkinter as tk
import hashlib
import json

password_show = False

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


def on_add():
    password = password_entry.get()
    if check_password(password):
        print("Password Allowed")
    else:
        print("Invalid password. It must contain at least 8 characters, one lowercase letter, one uppercase letter, one number and one special character (!, @, #, $, %, ^, &, *).")
        return
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


def on_clear():
    password_list.delete(0, tk.END)


def on_show():
    with open("passwords.json", "r") as file:
        data = json.load(file)
        for key, value in data.items():
            password_list.insert(tk.END, key + " : " + value)


def show_clear():
    global password_show
    if password_show == False:
        password_entry.configure(show="")
        password_show = True
    else:
        password_entry.configure(show="*")
        password_show = False


def on_exit():
    exit()


root = tk.Tk()
root.title("Password Manager")
root.geometry("650x300")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=0, column=1, pady=20)

show_current_password = tk.Button(root, text="Show", command=show_clear)
show_current_password.grid(row=0, column=2)

add_button = tk.Button(root, text="Add Password", command=on_add)
add_button.grid(row=0, column=3)

show_button = tk.Button(root, text="Show Passwords", command=on_show)
show_button.grid(row=2, column=0)

clear_button = tk.Button(root, text="Clear Passwords", command=on_clear)
clear_button.grid(row=2, column=1)

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.grid(row=2, column=4)

password_list = tk.Listbox(root, width=100)
password_list.grid(row=1, column=0, columnspan=10)

root.mainloop()


root.mainloop()