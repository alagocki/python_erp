import mysql.connector
from mysql.connector import errorcode


class databaseClass:

    @staticmethod
    def create_connection():
        cnx = None
        try:
            cnx = mysql.connector.connect(user='root',
                                          password='devpass',
                                          host='127.0.0.1',
                                          port='3307',
                                          database='tg_wawision')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        # else:
        #    cnx.close()

        return cnx
