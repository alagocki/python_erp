from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QMainWindow

from PyQt6.QtWidgets import QWidget


class AbstractClass(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()