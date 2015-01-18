from src.model import MyModel
from src.view import MyView

__author__ = 'mwech'

import sys
from PyQt4 import QtGui

class MyController(QtGui.QWidget):
    def __init__(self):
        self.model = MyModel()
        self.view = MyView()

    def main(self):
        QtGui.QWidget.__init__(self)
        self.view.setupUi(self)


app = QtGui.QApplication(sys.argv)
c = MyController()
c.main()
sys.exit(app.exec_())