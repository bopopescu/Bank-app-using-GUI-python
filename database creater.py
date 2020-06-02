import mysql.connector

conn=mysql.connector.connect(host='127.0.0.1',user="root", password="",database="JK_bank")

mycursor=conn.cursor()

# Lines to create data base no Longer needed
# mycursor.execute("CREATE DATABASE JK_bank")
# conn.commit()

#step 2 Create a Table
#user_id - Int --> primary key -->Not Null --Aout Incremect
#Name - Varchar -- Not NuLL
#email - Varchar --NOT NULL
#password - Varchar --Not Null

# mycursor.execute("CREATE TABLE users (user_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)")
# conn.commit()


#mycursor.execute("INSERT INTO users (user_id, name, email, password) VALUES (NULL, 'Jwed Akhtar','jk97@gmail.com','9709')")
#conn.commit()

# Retrieve
#mycursor.execute("SELECT * FROM users")
#data=mycursor.fetchall()

#for i in data:
    #print(i)
# Update
#mycursor.execute("UPDATE users SET password='virat' WHERE user_id=1")
#conn.commit()

# Delete
#mycursor.execute("DELETE FROM users WHERE user_id=3")
#conn.commit()