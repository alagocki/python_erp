import sys

from PyQt6 import QtSql
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from classes.abstract_class import AbstractClass

from classes.article import Article
from GUI.frm_main import Ui_frm_main
from classes.customer import Customer


class FrmMain(QMainWindow, Ui_frm_main, AbstractClass):
    def __init__(self):
        super().__init__()
        self.frm_article = None
        self.setupUi(self)

        self.func_mappingSignal()

    def func_mappingSignal(self):
        self.actionClose.triggered.connect(self.close_win)
        self.actionArticle_List.triggered.connect(lambda: self.open_win(Article))
        self.actionCustomer_List.triggered.connect(lambda: self.open_win(Customer))

    def open_win(self, Obj):
        self.frame = Obj()
        self.frame.show()


def create_connection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("Database/tg_wawision")

    if not db.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % db.lastError().databaseText(),
        )
        return False
    return True


if not create_connection():
    sys.exit(1)


def main():
    app = QApplication(sys.argv)
    frm_main = FrmMain()

    frm_main.show()

    app.exec()


if __name__ == '__main__':
    main()
