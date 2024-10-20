import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="swap22...",
    # database=""
)

print(mydb.get_server_info())

mycursor = mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)
