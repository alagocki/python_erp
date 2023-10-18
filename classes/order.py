import sqlite3

from PyQt6 import QtSql

from classes.abstract_class import AbstractClass
from classes.helper_class import HelperClass

from GUI.frm_order import Ui_frm_order
from Services.messageService import MessageService


class Order(Ui_frm_order, AbstractClass):
    def __init__(self):
        super().__init__()
        self.ms = MessageService()
        self.setupUi(self)
        self.mod_order_list = QtSql.QSqlRelationalTableModel()
        #self.mod_order_list.setTable("order")
        self.mod_order_list.setQuery("""select 
                                            o.datum as Datum, 
                                            o.internet as Bestellnr, 
                                            o.belegnr as Beleg,
                                            o.gesamtsumme as Betrag, 
                                            o.status as Status,
                                            o.liefername as Liefername,
                                            o.lieferstrasse as Lieferstrasse,
                                            o.lieferplz as LieferPLZ,
                                            o.lieferort as Lieferort,
                                            o.lieferland as Lieferland,
                                            o.zahlungsweise as Zahlungsweise,
                                            o.name as Name
                                        from 'order' o""")
        self.mod_order_list.select()
        self.tbl_order_list.setModel(self.mod_order_list)

        self.func_mappingSignal()

    def func_mappingSignal(self):
        self.btn_order_list_close.clicked.connect(lambda: HelperClass.close_win(self))




