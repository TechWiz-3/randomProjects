import mysql.connector

db = mysql.connector.connect(
    host="redacted",
    user="redacted",
    password="redacted",
    port="redacted",
    database = "redacted",
        )

cursor = db.cursor(buffered=True)

