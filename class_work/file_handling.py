# file = open("my_name.txt", "w")
# file.write("Zachary Youssef\n")
# file.close()
# file = open("my_name.txt", "a")
# file.write("Qualification: Networking Genius\n")
# file.write("Subject: Programming\n")
# file.write("Status: a little bit sleepy")
# file.close()

import os.path as path

if path.exists("my_name.txt"):
    file = open("my_name.txt", "r")
    print(file.read())
else:
    print("File not found")