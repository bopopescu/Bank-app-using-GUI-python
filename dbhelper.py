import mysql.connector

class DBHelper:

    def __init__(self):
        # connect to the database
        try:
            self._conn=mysql.connector.connect(host="127.0.0.1", user="root", password="", database="JK_bank")
            self._mycursor=self._conn.cursor()
        except:
            print("Could not connect to database")
            exit()

    def check_login(self, account_num, password):

        # Perform login
        self._mycursor.execute(
            "SELECT * FROM users WHERE account_num LIKE '{}' AND password LIKE '{}'".format(account_num, password))
        data = self._mycursor.fetchall()

        return data


    def fetch_userdata(self,user_id):

        self._mycursor.execute("SELECT * FROM users WHERE user_id LIKE {}".format(user_id))
        data = self._mycursor.fetchall()

        return data



    def register(self, name, account_num, password, age, gender, city, amount, dp):

            try:

                self._mycursor.execute("""
                                                        INSERT INTO users (user_id,name,account_num,password,age,gender,city,amount,dp)
                                                        VALUES
                                                        (NULL, '{}','{}','{}',{},'{}','{}','{}','{}')
    """.format(name, account_num, password, age, gender, city, amount, dp))

                self._conn.commit()
                return 1
            except:
                return 0

    def update_info(self, gender, age, city, user_id):
        try:
            print("""
                                        UPDATE users SET gender='{}',age={},city='{}'
                                        WHERE user_id LIKE {}
    """.format(gender, age, city, user_id))
            self._mycursor.execute("""
                                        UPDATE users SET gender='{}',age={},city='{}'
                                        WHERE user_id LIKE {}
    """.format(gender, age, city, user_id))
            self._conn.commit()
            return 1
        except:
            return 0

    def update_amount(self, amount, user_id):
        try:
            print("""
                                        UPDATE users SET amount='{}'
                                        WHERE user_id LIKE {}
    """.format(amount, user_id))
            self._mycursor.execute("""
                                        UPDATE users SET amount='{}'
                                        WHERE user_id LIKE {}
    """.format(amount, user_id))
            self._conn.commit()
            return 1
        except:
            return 0









