from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtWidgets import QWidget


class helperClass(QMainWindow, QWidget):

    @staticmethod
    def open_win(self, Obj):
        self.frame = Obj()
        self.frame.show()

    @staticmethod
    def close_win(self):
        self.close()

    @staticmethod
    def create_pagination(self, layout, cnt):
        for i in range(10):
            if i < 6:
                btn = QPushButton(parent=self)
                btn.setText(str((i + 1) * 10))
                btn.setFixedSize(40, 50)
                layout.addWidget(btn)

        label = QLabel(parent=self)
        label.setStyleSheet("font-size: 30px")
        label.setText(" ... ")
        label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(label)

        pages = cnt // helperClass.get_items_per_page()
        btn = QPushButton(parent=self)
        btn.setText(str(pages))
        btn.setFixedSize(40, 50)
        layout.addWidget(btn)

    @staticmethod
    def get_items_per_page():
        return 250
