from abc import ABC, abstractmethod

from PyQt6.QtWidgets import QWidget


class AbstractClass(QWidget):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def close_win(self):
        self.close()
