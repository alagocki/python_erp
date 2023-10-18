import sqlite3

from PyQt6 import QtSql, QtGui

from classes.abstract_class import AbstractClass
from classes.helper_class import HelperClass

from GUI.frm_customer import Ui_frm_customer
from Services.messageService import MessageService


class Customer(Ui_frm_customer, AbstractClass):
    def __init__(self):
        super().__init__()
        self.ms = MessageService()
        self.setupUi(self)
        self.mod_customer_list = QtSql.QSqlRelationalTableModel()
        self.mod_customer_list.setTable("customer")
        self.mod_customer_list.select()

        self.tbl_customer_list.setModel(self.mod_customer_list)

    def func_mappingSignal(self):
        self.btn_customer_list_close.clicked.connect(lambda: HelperClass.close_win(self))