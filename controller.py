from model import Model
from nonogram_ui import Ui_Dialog
from view import View
from PyQt4 import QtCore, QtGui
import sys
__author__ = 'mwech'
class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View()

    def main(self):
        QtGui.QWidget.__init__(self)
        self.view.setupUi(self)
        app = QtGui.QApplication(sys.argv)
        ex = Ui_Dialog()
        ex.show()
        sys.exit(app.exec_())

c = Controller()
c.main()