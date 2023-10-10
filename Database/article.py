import sys

from PyQt6 import QtSql
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QWidget, QTableWidgetItem

from GUI.frm_article import Ui_frm_article


class article(QWidget, Ui_frm_article):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mod_article_list = QtSql.QSqlRelationalTableModel()

        self.mod_article_list.setQuery("select a.id as ID, a.nummer as SKU, a.name_de as Bezeichnung from article a")
        self.mod_article_list.select()
        self.tbl_article_list.setModel(self.mod_article_list)

        self.btn_article_list_close.clicked.connect(self.close_win)


        #self.tbl_article_list_2.setColumnCount(3)
        #self.tbl_article_list_2.setHorizontalHeaderLabels(["ID", "SKU", "Bezeichnung"])
        #query = QSqlQuery("select a.id as ID, a.nummer as SKU, a.name_de as Bezeichnung from article a")
        #while query.next():
        #    rows = self.tbl_article_list_2.rowCount()
        #    self.tbl_article_list_2.setRowCount(rows + 1)
        #    self.tbl_article_list_2.setItem(rows, 0, QTableWidgetItem(query.value(0)))
        #    self.tbl_article_list_2.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
        #    self.tbl_article_list_2.setItem(rows, 2, QTableWidgetItem(query.value(2)))
        #self.tbl_article_list_2.resizeColumnsToContents()

    def func_mappingSignal(self):
        self.tbl_article_list.clicked.connect(self.func_test)

    def func_test(self, item):
        index = self.tbl_article_list.currentIndex().siblingAtColumn(0)
        article_id = index.data()
        print(article_id)

    def close_win(self):
        self.close()

