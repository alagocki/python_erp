from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget


class HelperClass(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

    @staticmethod
    def open_win(self, Obj):
        self.frame = Obj()
        self.frame.show()

    @staticmethod
    def close_win(self):
        self.close()

