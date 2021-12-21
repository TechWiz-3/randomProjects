import mysql.connector
mydb = mysql.connector.connect(
  host="containers-us-west-23.railway.app",
  user="root",
  password="yUWgeMOav9HmGFDqUIXo",
  database="railway",
  port="6499"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# mycursor.execute("CREATE TABLE test_goals_2002 (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), goals VARCHAR(255))")
person = "ctx.user"
goal = input("What's your new years goal: ")
# finalValues = f'"{person}", "{goal}"'
finalValues = (person, goal)
print(finalValues)
sql = "INSERT INTO test_goals_2002 (user, goals) VALUES (%s, %s)"
mycursor.execute(sql, finalValues)
mydb.commit()
# mycursor.execute()

