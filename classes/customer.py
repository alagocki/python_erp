import sqlite3

from PyQt6 import QtSql, QtGui

from classes.abstract_class import AbstractClass

from GUI.frm_customer import Ui_frm_customer
from Services.messageService import MessageService


class Customer(Ui_frm_customer, AbstractClass):
    def __init__(self):
        super().__init__()
        self.ms = MessageService()
        self.setupUi(self)
        self.mod_customer = QtSql.QSqlRelationalTableModel()
        self.mod_customer.setTable("customer")
        self.mod_customer.select()

        self.tbl_customer_list.setModel(self.mod_customer)
