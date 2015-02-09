import sys
from PyQt4 import QtGui
from src.MVC.controller import MyController
from src.MVC.model import MyModel

"""
@author: Muhammed Kanyildiz, Maximilian Wech
@version: 20150209
@description: Main / Programmausführung
"""

app = QtGui.QApplication(sys.argv)
m = MyModel()
#Aufruf des Controllers
c = MyController(m)
#Ausführen der main Methode in der Controller Klasse
c.main()
#Programmende
sys.exit(app.exec_())

