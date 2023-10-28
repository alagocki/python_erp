from Helper.database_class import databaseClass
import mysql
from PyQt6.QtSql import QSqlQuery
from mysql.connector import errorcode

from Helper.helper_class import helperClass


class articleRepository:

    def get_article_by_id(self, id):
        article_id = str(id)
        query_string = "select a.* from article a where a.id = " + article_id
        return self.prepare_single_result(query_string)

    def get_article_by_sku(self, sku):
        article_sku = str(sku)
        query_string = "select a.* from article a where a.nummer = '" + article_sku + "'"
        return self.prepare_single_result(query_string)

    def get_all_article(self):

        try:
            connection = databaseClass.create_connection()
            with (connection.cursor() as cursor):
                cursor.execute(
                    "select a.id, a.nummer, a.hersteller, a.ean, a.fx_erstellt_am, a.name_de from artikel a limit 0, " + str(helperClass.get_items_per_page()))
                rows = cursor.fetchall()
                return rows
        except (mysql.connector.Error, IOError) as err:
            raise err

    def prepare_single_result(self, query_string):
        self.query = QSqlQuery(query_string)
        self.columns = self.query.record().count()

        self.query.first()

        self.result = []
        while self.query.isValid():
            record = [self.query.value(index) for index in range(self.columns)]
            self.result.append(record)
            self.query.next()

        return self.result

    def get_article_quantity(self):
        try:
            connection = databaseClass.create_connection()
            with (connection.cursor() as cursor):
                cursor.execute(
                    "select count(*) from artikel a")
                return cursor.fetchone()[0]
        except (mysql.connector.Error, IOError) as err:
            raise err
