import pymysql
import pymysql.cursors
from sqlmodel import Session, create_engine

engine = create_engine("mysql+pymysql://root:devpass@localhost:3307/tg_wawision", echo=True)

class databaseClass:

    @staticmethod
    def create_connection():
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     port=3307,
                                     user='root',
                                     password='devpass',
                                     database='tg_wawision',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        return connection