__author__ = 'mwech'
from PyQt4 import QtCore, QtGui
from src.view import MyView
class MyModel():
    def __init__(self):
        self.view = MyView()
    def neustart(self):
        for j in range(15):
            for i in range(15):
                list = [j, i]
                self.view.tableWidget_2.setItem(j,i,QtGui.QTableWidgetItem())
                self.view.tableWidget_2.item(j,i).setBackground(QtGui.QColor('white'))

    def cell_was_clicked(self, row, column):
        list = [row, column]
        if list in self.view.liste:
            self.view.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
            item = self.view.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('white'))
            a = self.view.liste.index(list)
            del self.view.liste[a]
        else:
            self.view.liste.append([row, column])
            self.view.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
            item = self.view.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('black'))

    def loesung(self):
        self.neustart()
        list = [[0,8],[0,9],
                        [1,2],[1,3],[1,7],[1,8],[1,9],
                        [2,1],[2,3],[2,4],[2,6],[2,7],[2,8],[2,9],
                        [3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],
                        [4,2],[4,3],[4,4],[4,5],[4,6],[4,7],
                        [5,3],[5,4],[5,5],[5,6],[5,7],[5,8],
                        [6,4],[6,5],[6,6],[6,7],[6,8],[6,9],
                        [7,3],[7,5],[7,7],[7,8],[7,9],
                        [8,8],[8,9],
                        [9,7],[9,8]]
        for z in range(len(list)):
            self.cell_was_clicked(list[z][0], list[z][1])