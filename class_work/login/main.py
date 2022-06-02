def main():
    login = input("Enter your login: ")
    password = input("Enter your password: ")
    allow_entry = False
    with open("accounts.txt", "r") as accounts_file:
        for line in accounts_file:
            login_passwd = line.split(" ")
            if password == login_passwd[1]:
                allow_entry = True
    if allow_entry == True:
        print("Welcome")
    else:
        print("Wrong password brug")
    
if __name__ == "__main__":
    main()
