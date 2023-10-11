from PyQt6 import QtGui


class MessageService():

    def __init__(self):
        super().__init__()

    def set_message(self, message, lable):
        color = QtGui.QColor(255, 0, 0)
        alpha = 200
        values = "{r}, {g}, {b}, {a}".format(r=color.red(),
                                             g=color.green(),
                                             b=color.blue(),
                                             a=alpha)
        lable.setStyleSheet("QLabel {color: rgba(" + values + "); }")
        lable.setText(message)