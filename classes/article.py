from PyQt6 import QtSql, QtGui
from PyQt6.QtWidgets import QWidget

from GUI.frm_article import Ui_frm_article
from Repository.article_repository import article_repository


class article(QWidget, Ui_frm_article):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mod_article_list = QtSql.QSqlRelationalTableModel()

        self.mod_article_list.setQuery("select a.id as ID, a.nummer as SKU, a.name_de as Bezeichnung from article a")
        self.mod_article_list.select()
        self.tbl_article_list.setModel(self.mod_article_list)

        self.func_mappingSignal()

    def func_mappingSignal(self):
        self.tbl_article_list.clicked.connect(self.set_artickle_details)
        self.btn_article_list_close.clicked.connect(self.close_win)
        self.btn_search_article.clicked.connect(self.get_article_details_by_search)
        #self.btn_search_article.clicked.connect(lambda: self.set_message(message))

    def set_message(self, message):
        color = QtGui.QColor(255, 0, 0)
        alpha = 200
        values = "{r}, {g}, {b}, {a}".format(r=color.red(),
                                             g=color.green(),
                                             b=color.blue(),
                                             a=alpha)
        self.lb_messages.setStyleSheet("QLabel {color: rgba(" + values + "); }")
        self.lb_messages.setText(message)

    def set_artickle_details(self, item):
        index = self.tbl_article_list.currentIndex().siblingAtColumn(0)
        article_id = index.data()
        self.get_article_details(article_id)

    def get_article_details(self, id):
        ar = article_repository()
        article_data = ar.get_article_by_id(id)
        self.input_sku_edit.setText(str(article_data[0][1]))
        self.input_name_edit.setText(article_data[0][3])
        self.text_description_edit.setText(article_data[0][5])

    def get_article_details_by_search(self):
        self.sku = self.ln_search_article.text()
        if self.sku == '':
            self.set_message("Bitte gültige SKU angeben")
        else:
            ar = article_repository()
            article_data = ar.get_article_by_sku(self.sku)

            if not article_data:
                self.set_message("Artikel wurde nicht gefunden")
            else:
                self.input_sku_edit.setText(str(article_data[0][1]))
                self.input_name_edit.setText(article_data[0][3])
                self.text_description_edit.setText(article_data[0][5])

    def clear_article_details(self):
        self.input_sku_edit.setText("")
        self.input_name_edit.setText("")
        self.text_description_edit.setText("")

    def close_win(self):
        self.close()
