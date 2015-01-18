__author__ = 'Muhammed5'
import os
from PyQt4 import QtCore, QtGui
import sys

class Model():
    def neustart(self):
        for j in range(15):
            for i in range(15):
                list = [j, i]
                self.tableWidget_2.setItem(j,i,QtGui.QTableWidgetItem())
                self.tableWidget_2.item(j,i).setBackground(QtGui.QColor('white'))

    def cell_was_clicked(self, row, column):
        list = [row, column]
        self.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
        item = self.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('black'))
       # print("Row %d and Column %d was clicked" % (row, column))