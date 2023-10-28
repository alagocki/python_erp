import sys
from PyQt6.QtWidgets import QApplication

from Classes.abstract_class import abstractClass
from Helper.helper_class import helperClass

from Classes.article import article
from Classes.customer import customer
from Classes.order import order
from GUI.frm_main import Ui_frm_main


class FrmMain(Ui_frm_main, abstractClass):
    def __init__(self):
        super().__init__()
        self.frm_article = None
        self.setupUi(self)

        self.func_mappingSignal()

    def func_mappingSignal(self):
        self.actionClose.triggered.connect(lambda: helperClass.close_win(self))
        self.btn_close_main.clicked.connect(lambda: helperClass.close_win(self))
        self.actionArticle_List.triggered.connect(lambda: helperClass.open_win(self, article))
        self.actionCustomer_List.triggered.connect(lambda: helperClass.open_win(self, customer))
        self.actionOrder_List.triggered.connect(lambda: helperClass.open_win(self, order))

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
