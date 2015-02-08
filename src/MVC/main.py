import sys

from PyQt4 import QtGui

from src.MVC.controller import MyController

__author__ = 'Muhammed5'



app = QtGui.QApplication(sys.argv)
c = MyController()
c.main()
sys.exit(app.exec_())

