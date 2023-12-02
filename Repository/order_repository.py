import Model.order
from Helper.database_class import databaseClass
import mysql
from mysql.connector import errorcode

from Helper.helper_class import helperClass


class orderRepository:

    def get_all_data(database: str):
        try:
            connection = databaseClass.create_connection()
            with (connection.cursor() as cursor):
                cursor.execute(
                    "select a.* from " + database + " a order by id desc limit 0, " + str(helperClass.get_items_per_page()))
                rows = cursor.fetchall()
                return rows
        except (mysql.connector.Error, IOError) as err:
            raise err