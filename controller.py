from model import Model
from nonogram_ui import Ui_Dialog
from view import View

__author__ = 'Muhammed5'
import os
from PyQt4 import QtCore, QtGui
import sys

class Controller:
    def __init__(self, app):
        self.model = Model()
        self.view = View(None)

        app = QtGui.QApplication(sys.argv)
        ex = Ui_Dialog()
        ex.show()
        sys.exit(app.exec_())