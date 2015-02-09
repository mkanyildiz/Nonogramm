import sys
from PyQt4 import QtGui
from src.VC.controller import MyController

"""
@author: Muhammed Kanyildiz, Maximilian Wech
@version: 20150209
@description: Main / Programmausführung
"""

app = QtGui.QApplication(sys.argv)
#Aufruf des Controllers
c = MyController()
#Ausführen der main Methode in der Controller Klasse
c.main()
#Programmende
sys.exit(app.exec_())

