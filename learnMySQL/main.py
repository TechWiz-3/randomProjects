import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("password")

mydb = mysql.connector.connect(
  host="containers-us-west-23.railway.app",
  user="root",
  password=password,#sus person, why are you reading this line??
  database="railway",
  port="6499"
)

mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM test_goals_2002 ORDER BY goals;")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

#mycursor.execute("CREATE TABLE how_often (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), days VARCHAR(255))")
# person = "ctx.user"
# goal = input("What's your new years goal: ")
# finalValues = (person, goal)
# print(finalValues)
# sql = "INSERT INTO test_goals_2002 (user, goals) VALUES (%s, %s)"
# mycursor.execute(sql, finalValues)
# mydb.commit()
# # mycursor.execute()
# mycursor.execute("CREATE TABLE how_often_2 (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), days SMALLINT UNSIGNED)")
person = "ZactheWise1235"
time = 10
finalValues = (person, time)
print(finalValues)
sql = "INSERT INTO how_often_2 (user, days) VALUES (%s, %s)"
mycursor.execute(sql, finalValues)
mydb.commit()

person = "ZacTheWise2#8449"
time = 22
finalValues = (person, time)
sql = "INSERT INTO how_often_2 (user, days) VALUES (%s, %s)"
mycursor.execute(sql, finalValues)
mydb.commit()


mycursor.execute("SELECT * FROM how_often_2")

for entry in mycursor:
  print(entry)
  # if "ZacTheWise#1234" in entry:
  #   print("")

