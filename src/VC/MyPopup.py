import sys
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui

__author__ = 'Muhammed5'
class MyPopup(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        layout = QtGui.QVBoxLayout(self)
        self.edit = QtGui.QTextEdit()
        self.edit.setFontPointSize(20)
        self.edit.insertPlainText('GAME OVER')
        layout.addWidget(self.edit)
