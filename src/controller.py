from src.view import MyView
from src.model import MyModel
__author__ = 'mwech'

import sys
from PyQt4 import QtGui

class MyController():
    def __init__(self):
        self.view = MyView()
        self.model = MyModel()

    def main(self):
        self.view.show()
        self.view.pushButton_2.clicked.connect(self.model.neustart)
        self.view.tableWidget_2.cellClicked.connect(self.model.cell_was_clicked)
        self.view.pushButton.clicked.connect(self.model.loesung)



