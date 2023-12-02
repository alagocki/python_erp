from mysql.connector.logger import logger
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from Classes.abstract_class import abstractClass
from Helper.helper_class import helperClass
from GUI.frm_order import Ui_frm_order
from Repository.order_repository import orderRepository
from Services.message_service import messageService
from Model.order import create_db_and_tables_orders
from Helper.table_helper_class import tableHelperClass
import yaml


class order(Ui_frm_order, abstractClass):

    def __init__(self):
        super().__init__()
        self.model = None
        self.ms = messageService()
        self.setupUi(self)

        create_db_and_tables_orders()

        self.func_mappingSignal()
        self.data_view()

    def func_mappingSignal(self):
        self.btn_order_list_close.clicked.connect(lambda: helperClass.close_win(self))

    def data_view(self):
        try:
            model = tableHelperClass.get_table(self, 'order', orderRepository)
            self.tbl_order_list.setModel(model)
        except Exception as err:
            logger.exception('Failed: ' + str(err))
