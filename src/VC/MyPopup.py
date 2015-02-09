import sys
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui

"""
@author: Muhammed Kanyildiz, Maximilian Wech
@version: 20150209
@description: In dieser Klasse wird ein Game Over Fenster erstellt, falls der Benutzer das Spiel verliert.
"""
class MyPopup(QtGui.QWidget):

    def __init__(self):
        """
        Konstruktor
        """
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.edit = QtGui.QTextEdit()
        self.edit.setFontPointSize(20)
        self.edit.insertPlainText('GAME OVER')
        layout.addWidget(self.edit)
