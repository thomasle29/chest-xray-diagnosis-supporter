import mysql.connector
from mysql.connector import MySQLConnection, Error
import Config.reader as reader

class SQL:
    def MySQL_CONFIG(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()

    def call_procedure(self, name_proc, args):
        result = tuple()
        try:
            self.cursor.callproc("pro_login", args)
            for res in self.cursor.stored_results():
                result = tuple(res.fetchall())
        except Error as e:
            print(e)
        return result

MySQL = SQL()