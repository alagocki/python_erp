import sys

from PyQt6 import QtSql
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from classes.article import article
from GUI.frm_main import Ui_frm_main


class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionBeenden.triggered.connect(self.close_win)
        self.actionArtikel_Liste.triggered.connect(self.open_article_win)
        self.frm_article = article()

    def open_article_win(self):
        self.frm_article.show()

    def close_win(self):
        self.close()


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
    frm_main = Frm_main()

    frm_main.show()

    app.exec()


if __name__ == '__main__':
    main()
