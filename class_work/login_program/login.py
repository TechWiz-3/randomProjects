# Created by Zac
# 31/05/2022
# Login program with numerous options

# General Imports
from sys import exit  # method to exit script
from time import sleep  # method to stop script for seconds
# Password Generation Imports 
from string import ascii_letters, digits  # attributes that contain strings with all the ascii letters or digits
from os import urandom  # produces random bytes suitable for cryptography
from random import seed, choice  # seed initialises the random no generator,  choice chooses from a random element from a sequence

def menu():
    """Displays select menu and returns users choice"""
    menu = "1) Login\n2) Register\n3) View Accounts\n4) Exit\n"
    option = int(input(menu))  # prints memu and gets user input
    # depending on user input, the function will return a string describing
    # what the user wishes to do
    print("\n") # add some space
    if option == 1:  # option 1 in select menu
        return "login"
    elif option == 2:  # option 2 in select menu
        return "register"
    elif option == 3:
        return "view"
    elif option == 4:  # option 4 in select menu
        sleep(2)
        return exit()  # exit the program


def login():
    usr = input("Enter your username: ")
    passwd = input("Enter your password: ")
    with open("accounts.txt", "r") as accounts:  # open the accounts file
        for line in accounts:  # loop through the lines in the file
            login_passwd = line.replace("\n", "").split(" ")  # store the login and password in
            # compare provided login to the login program is looping through
            if usr == login_passwd[0]:
                if passwd == login_passwd[1]:
                    print("Welcome")
                    return
                else:  # wrong password
                    print("Password wrong, please try again.")
                    # enter a password re-try loop
                    passwd = input("Enter your password: ")
                    while passwd != login_passwd[1] and passwd.lower() != "x":
                        print("Password wrong, please try again (press X to quit).")
                        passwd = input("Enter your password: ")
                    if passwd.lower() == "x":  # user exited password loop
                        print("Exiting")
                        sleep(2)
                        exit()
                    else:  # password entry was successful
                        print("Welcome")
                        return
            else:
                continue  # continue in the for loop scanning the accounts document

def register():
    """allows users to register a new account"""
    cont = input("You will be prompted to register a new account, do you wish to continue? [y/n] ")
    if cont.lower() == "y":
        name = input("Enter your new account's name: ")
        password_type = input("Would you like to create your own password [a] or have one automatically generated [b]? ")
        if password_type.lower() == "a":
            # allow user to generate own password
            passwords_match = False
            while not passwords_match:  # while the passwords don't match, prompt for new ones
                password = input("Your password here: ")
                confirm_password = input("Confirm your password here: ")
                if password == confirm_password:
                    print("Passwords match")
                    passwords_match = True
                    create_acc(name, password)  # log the new account
                else:
                    print("Passwords don't match, please try again")
        elif password_type.lower() == "b":
            # auto generate a password
            type_recognised = False
            while type_recognised == False:
                choose_type = input("All characters [a]\nAll numbers [b]\nAll special characters[c]\nCombination[d]\nFrom the options above, list the password type you wish to have generated: ")
                choose_length = int(input("Enter the password length you require (4-20) "))
                if choose_type.lower() == "a":
                    password = rand_passwd("char", choose_length)
                    type_recognised = True
                elif choose_type.lower() == "b":
                    password = rand_passwd("num", choose_length)
                    type_recognised = True
                elif choose_type.lower() == "c":
                    password = rand_passwd("schar", choose_length)
                    type_recognised = True
                elif choose_type.lower() == "d":
                    password = rand_passwd("all", choose_length)
                    type_recognised = True
                else:
                    print("Type not recognised, try agan")
                create_acc(name, password)  # log account
    else:
        pass
        menu()  # loop back to the select menu


def rand_passwd(typ: str, length: int) -> str:
    """generates a fully random password and returns it, used in register function"""
    password = ""
    if typ == "char":  # use only characters
        chars = ascii_letters
        seed = (urandom(1024))
        for i in range(length):
            password += choice(chars)  # append a random pick of character to the password
    elif typ == "num":  # use only numbers
        chars = digits
        seed = (urandom(1024))
        for i in range(length):
            password += choice(chars)
    elif typ == "schar":  # use only special characters
        chars = "!@#$%^&*\(\)"
        seed = (urandom(1024))
        for i in range(length):
            password += choice(chars)
    elif typ == "all":  # use all three
        chars = f"{ascii_letters}{digits}!@#$%^&*\(\)"
        seed = (urandom(1024))
        for i in range(length):
            password += choice(chars)
    return password

def create_acc(name: str, passwd: str):
    """function that writes to the accounts file for new account entries, used in regiister function"""
    try:
        with open("accounts.txt", "a") as accounts:
            new_account = f"{name} {passwd}\n"
            accounts.write(new_account)
    except FileNotFoundError:  # if the fle cannot be found
        print("The accounts file cannot be found in this directory")
    except Exception as error:
        print("Error occured: ", error)
    else:
        print("New account created successfully")
        sleep(2)
        pass
        menu_loop()


def view_accs():
    """prints account information"""
    line_count = 0
    try:
        with open("accounts.txt", "r") as accounts:
            for line in accounts:  # loop through lines in file
                print(line)
                line_count += 1  # increment line count by one
            print(f"Accounts: {line_count}\n")
    except FileNotFoundError:
        print("File not found in this directory")

def menu_loop():
    """function that is called to run the select menu"""
    while True:  # broken by control C or pressing 4 for exit
            option = menu()
            if option == "login":
                login()
            elif option == "register":
                register()
            elif option == "view":
                view_accs()

if __name__ == "__main__":
    print("Welcome to your login program, enter the number corresponding to the action list below you would like to take\n") 
    menu_loop()

