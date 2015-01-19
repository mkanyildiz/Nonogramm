from src.view import MyView
from src.model import MyModel
__author__ = 'mwech'

import sys
from PyQt4 import QtGui

class MyController(QtGui.QWidget):
    def __init__(self):
        self.view = MyView()
        self.model = MyModel()

    def main(self):
        QtGui.QWidget.__init__(self)
        self.view.setupUi(self)
        self.model.methode()


app = QtGui.QApplication(sys.argv)
c = MyController()
c.main()
sys.exit(app.exec_())