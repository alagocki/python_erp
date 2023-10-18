from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QMainWindow

from PyQt6.QtWidgets import QWidget


class AbstractClass(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def open_win(self, Obj):
        self.frame = Obj()
        self.frame.show()

    @abstractmethod
    def close_win(self):
        self.close()
