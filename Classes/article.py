import sqlite3

import mysql
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from mysql.connector.logger import logger

from Classes.abstract_class import abstractClass
from Helper.helper_class import helperClass

from GUI.frm_article import Ui_frm_article
from Repository.article_repository import articleRepository
from Services.message_service import messageService


class article(Ui_frm_article, abstractClass):
    def __init__(self):
        super().__init__()

        self.ms = messageService()
        self.setupUi(self)
        self.data_view()


    def func_mappingSignal(self):
        self.tbl_article_list.clicked.connect(self.set_artickle_details)
        self.btn_article_list_close.clicked.connect(lambda: helperClass.close_win(self))
        self.btn_search_article.clicked.connect(self.get_article_details_by_search)
        # self.btn_search_article.clicked.connect(lambda: self.set_message(message))

    def set_artickle_details(self, item):
        index = self.tbl_article_list.currentIndex().siblingAtColumn(0)
        article_id = index.data()
        print(article_id)
        # self.get_article_details_by_id(article_id)

    def get_article_details_by_id(self, id):
        ar = articleRepository()
        try:
            article_data = ar.get_article_by_id(id)
            self.input_sku_edit.setText(str(article_data[0][1]))
            self.input_name_edit.setText(article_data[0][3])
            self.text_description_edit.setText(article_data[0][5])
        except sqlite3.DatabaseError as err:
            self.ms.set_message("ERROR (DB): " + str(err), self.lb_messages)

    def get_article_details_by_search(self):
        self.ms.set_message("", self.lb_messages)
        self.sku = self.ln_search_article.text()
        if self.sku == '':
            self.ms.set_message("Bitte gültige SKU angeben", self.lb_messages)
        else:
            try:
                ar = articleRepository()
                article_data = ar.get_article_by_sku(self.sku)

                if not article_data:
                    self.ms.set_message("Artikel wurde nicht gefunden", self.lb_messages)
                else:
                    self.input_sku_edit.setText(str(article_data[0][1]))
                    self.input_name_edit.setText(article_data[0][3])
                    self.text_description_edit.setText(article_data[0][5])
            except sqlite3.DatabaseError as err:
                self.ms.set_message("ERROR (DB): " + str(err), self.lb_messages)

    def clear_article_details(self):
        self.input_sku_edit.setText("")
        self.input_name_edit.setText("")
        self.text_description_edit.setText("")

    def data_view(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'SKU', 'Hersteller', 'EAN', 'erstellt am', 'Bezeichnung'])

        try:
            rows = articleRepository.get_all_article(self)

            for row in rows:
                # print(row[2])
                rowsCnt = self.model.rowCount()
                self.model.setRowCount(rowsCnt + 1)

                self.model.setItem(rowsCnt, 0, QStandardItem(str(row[0])))
                self.model.setItem(rowsCnt, 1, QStandardItem(str(row[1])))
                self.model.setItem(rowsCnt, 2, QStandardItem(str(row[2])))
                self.model.setItem(rowsCnt, 3, QStandardItem(str(row[3])))
                self.model.setItem(rowsCnt, 4, QStandardItem(str(row[4])))
                self.model.setItem(rowsCnt, 5, QStandardItem(str(row[5])))

            self.tbl_article_list.setModel(self.model)

            cntArticle = articleRepository.get_article_quantity(self)

            helperClass.create_pagination(self, self.l_pagination_article, cntArticle)

        except Exception as err:
            logger.exception('Failed: ' + str(err))

