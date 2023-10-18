import sys
from PyQt6.QtWidgets import QApplication

from Classes.abstract_class import AbstractClass
from Helper.helper_class import HelperClass

from Classes.article import Article
from Classes.customer import Customer
from Classes.order import Order
from GUI.frm_main import Ui_frm_main


class FrmMain(Ui_frm_main, AbstractClass):
    def __init__(self):
        super().__init__()
        self.frm_article = None
        self.setupUi(self)

        self.func_mappingSignal()

    def func_mappingSignal(self):
        self.actionClose.triggered.connect(lambda: HelperClass.close_win(self))
        self.btn_close_main.clicked.connect(lambda: HelperClass.close_win(self))
        self.actionArticle_List.triggered.connect(lambda: HelperClass.open_win(self, Article))
        self.actionCustomer_List.triggered.connect(lambda: HelperClass.open_win(self, Customer))
        self.actionOrder_List.triggered.connect(lambda: HelperClass.open_win(self, Order))

    def open_win(self, Obj):
        self.frame = Obj()
        self.frame.show()


def main():
    app = QApplication(sys.argv)
    frm_main = FrmMain()

    frm_main.show()

    app.exec()


if __name__ == '__main__':
    main()
