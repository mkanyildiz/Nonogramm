from src.view import MyView

__author__ = 'mwech'

from PyQt4 import QtGui
#from src.view import MyView


class MyModel():
    def neustart(self):
        self.view = MyView()
        for j in range(15):
            for i in range(15):
                list = [j, i]
                self.view.tableWidget_2.setItem(j,i,QtGui.QTableWidgetItem())
                self.view.tableWidget_2.item(j,i).setBackground(QtGui.QColor('white'))

    def cell_was_clicked(self, row, column):
        list = [row, column]
        self.view.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
        item = self.view.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('black'))
       # print("Row %d and Column %d was clicked" % (row, column))