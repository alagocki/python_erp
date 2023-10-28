from PyQt6 import QtSql

from Classes.abstract_class import abstractClass
from Helper.helper_class import helperClass

from GUI.frm_customer import Ui_frm_customer
from Services.message_service import messageService


class customer(Ui_frm_customer, abstractClass):
    def __init__(self):
        super().__init__()
        self.ms = messageService()
        self.setupUi(self)
        self.mod_customer_list = QtSql.QSqlRelationalTableModel()
        self.mod_customer_list.setTable("customer")
        self.mod_customer_list.select()

        self.tbl_customer_list.setModel(self.mod_customer_list)

    def func_mappingSignal(self):
        self.btn_customer_list_close.clicked.connect(lambda: helperClass.close_win(self))