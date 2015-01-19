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
        print("Hallo")
        self.view.show()


