import mysql.connector
import sys
class DBhelper:
    def __init__(self):
        try:
            self.conn =  self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="hit_db_sql" )

            self.mycursor = self.conn.cursor()
        except:
            print("connection to MySQL database failed some errors occurd")
            sys.exit(2300)
        else:

            print("connecting to MySQL database")


    def register(self, name, email, password):

        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `gmail`, `password`) VALUES (NULL, "{}","{}","{}");
            """.format(name, email, password))
            self.conn.commit()
        except:
            return -1

        else:
            return 1

    def search(self,email, password):

        self.mycursor.execute("""
        SELECT * FROM users WHERE gmail LIKE '{}' and password LIKE '{}';
        """.format(email, password))

        data = self.mycursor.fetchall()

        print(data)

        return data