from PyQt4 import QtGui
from PyQt4.QtCore import QRect
from src.MVC import MyPopup
from src.MVC.MyPopup import Popup


"""
@author: Muhammed Kanyildiz, Maximilian Wech
@version: 20150209
@description: In dieser Klasse werden die Methoden für den Algorithmus des Spiels, sowie für die Interaktionen
              mit den GUI Elementen erstellt.
"""

class MyModel():
    """
    Attributes:
    view    Instanz der View Klasse
    """
    view = None
    level = ""
    def setView(self, MyView):
        """
        Eine neue View erstellen
        :param MyView: die View Klasse
        """
        self.view = MyView
        self.level = ""
    def neustart(self):
        """
        Mit dieser Methode werden alle im Array gespeicherten Felder gelöscht und die Spielfläche wird wieder ins
        Anfangsstadium zurückversetzt, sprich in weißer Farbe.
        """
        for j in range(15):
            for i in range(15):
                list = [j, i]
                self.view.tableWidget_2.setItem(j,i,QtGui.QTableWidgetItem())
                self.view.tableWidget_2.item(j,i).setBackground(QtGui.QColor('white'))
        self.level = self.view.comboBox.currentText()

        if self.level == "Medium":
            self.erg = [[0,8],[0,9],
                [1,2],[1,3],[1,7],[1,8],[1,9],
                [2,1],[2,3],[2,4],[2,6],[2,7],[2,8],[2,9],
                [3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],
                [4,2],[4,3],[4,4],[4,5],[4,6],[4,7],
                [5,3],[5,4],[5,5],[5,6],[5,7],[5,8],
                [6,4],[6,5],[6,6],[6,7],[6,8],[6,9],
                [7,3],[7,5],[7,7],[7,8],[7,9],
                [8,8],[8,9],
                [9,7],[9,8]]

        elif self.level == "Easy":
            self.erg = [[7,7]]

        elif self.level == "Hard":
            self.erg = [
                [0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],
                [1,2],[1,3],[1,5],[1,6],[1,7],[1,8],[1,9],[1,11],[1,12],
                [2,1],[2,2],[2,3],[2,4],[2,6],[2,7],[2,8],[2,10],[2,11],[2,12],[2,13],
                [3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,7],[3,9],[3,10],[3,11],[3,12],[3,13],[3,14],

                [4,0],[4,1],[4,2],[4,6],[4,7],[4,8],[4,12],[4,13],[4,14],
                [5,0],[5,1],[5,2],[5,6],[5,7],[5,8],[5,12],[5,13],[5,14],
                [6,0],[6,1],[6,2],[6,6],[6,7],[6,8],[6,12],[6,13],[6,14],
                [7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[7,9],[7,10],[7,11],[7,12],[7,13],[7,14],
                [8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8],[8,9],[8,10],[8,11],[8,12],[8,13],[8,14],
                [9,0],[9,1],[9,13],[9,14],

                [10,0],[10,1],[10,2],[10,12],[10,13],[10,14],
                [11,0],[11,1],[11,2],[11,3],[11,11],[11,12],[11,13],[11,14],
                [12,1],[12,2],[12,3],[12,4],[12,10],[12,11],[12,12],[12,13],
                [13,2],[13,3],[13,4],[13,5],[13,6],[13,7],[13,8],[13,9],[13,10],[13,11],[13,12],
                [14,3],[14,4],[14,5],[14,6],[14,7],[14,8],[14,9],[14,10],[14,11]
            ]
        self.fill_tab()
        self.liste = []

    def cell_clicked(self, row, column):
        """
        Diese methode ist der cell_was_clicked methode. Der einzige Unterschied liegt darin, dass wir hier nicht
        überprüfen, ob die Zelle bereits geklickt wurde, da dies beim "Lösung anzeigen" von Nachteil ist.
        :param row: die Zeilenzahl, in der sich die geklickte Zelle befindet
        :param column: die Spaltenzahl, in der sich die geklickte Zelle befindet
        """
        list = [row, column]
        self.liste.append([row, column])
        self.view.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
        item = self.view.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('black'))

    def cell_was_clicked(self, row, column):

        """
        Die Methode füllt eine Zelle mit schwarzer Farbe, falls eine Zelle angeklickt wurde. Des Weiteren wird die
        Zelle wieder weiß angemalt, falls diese bereits geklickt wurde.
        :param row: die Zeilenzahl, in der sich die geklickte zelle befindet
        :param column: die Spaltenzahl, in der sich die geklickte Zelle befindet
        """
        list = [row, column]
        self.cells_left()
        if list in self.liste:
            self.view.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
            item = self.view.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('white'))
            a = self.liste.index(list)
            del self.liste[a]
        else:
            self.liste.append([row, column])
            self.view.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
            item = self.view.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('black'))

        if self.liste == self.erg:
            self.w = Popup()
            self.w.setGeometry(QRect(100, 100, 400, 200))
            self.w.show()
            self.neustart()
            self.liste = []

    def loesung(self):
        """
        Zeigt die Lösung an; dabei werden die entsprechenden Felder schwarz angemalt.
        """
        self.level = self.view.comboBox.currentText()
        self.neustart()
        if self.level == "Medium":
            self.erg = [[0,8],[0,9],
                [1,2],[1,3],[1,7],[1,8],[1,9],
                [2,1],[2,3],[2,4],[2,6],[2,7],[2,8],[2,9],
                [3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],
                [4,2],[4,3],[4,4],[4,5],[4,6],[4,7],
                [5,3],[5,4],[5,5],[5,6],[5,7],[5,8],
                [6,4],[6,5],[6,6],[6,7],[6,8],[6,9],
                [7,3],[7,5],[7,7],[7,8],[7,9],
                [8,8],[8,9],
                [9,7],[9,8]]

        elif self.level == "Easy":
            self.erg = [[7,7]]

        elif self.level == "Hard":
            self.erg = [
                [0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],
                [1,2],[1,3],[1,5],[1,6],[1,7],[1,8],[1,9],[1,11],[1,12],
                [2,1],[2,2],[2,3],[2,4],[2,6],[2,7],[2,8],[2,10],[2,11],[2,12],[2,13],
                [3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,7],[3,9],[3,10],[3,11],[3,12],[3,13],[3,14],

                [4,0],[4,1],[4,2],[4,6],[4,7],[4,8],[4,12],[4,13],[4,14],
                [5,0],[5,1],[5,2],[5,6],[5,7],[5,8],[5,12],[5,13],[5,14],
                [6,0],[6,1],[6,2],[6,6],[6,7],[6,8],[6,12],[6,13],[6,14],
                [7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[7,9],[7,10],[7,11],[7,12],[7,13],[7,14],
                [8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8],[8,9],[8,10],[8,11],[8,12],[8,13],[8,14],
                [9,0],[9,1],[9,13],[9,14],

                [10,0],[10,1],[10,2],[10,12],[10,13],[10,14],
                [11,0],[11,1],[11,2],[11,3],[11,11],[11,12],[11,13],[11,14],
                [12,1],[12,2],[12,3],[12,4],[12,10],[12,11],[12,12],[12,13],
                [13,2],[13,3],[13,4],[13,5],[13,6],[13,7],[13,8],[13,9],[13,10],[13,11],[13,12],
                [14,3],[14,4],[14,5],[14,6],[14,7],[14,8],[14,9],[14,10],[14,11]
            ]
        for z in range(len(self.erg)):
            self.cell_clicked(self.erg[z][0], self.erg[z][1])

    def cells_left(self):
        """
        Diese Methode zeigt an, wie viele, noch nicht ausgewählte Felder, noch ausstehend sind.
        """


        z=len(self.erg)
        for i in range(len(self.erg)):
            #print(self.liste)
          #  if self.erg[i] not in self.liste:
         #     z += 1
            if self.erg[i] in self.liste:
                z -= 1

        self.view.lineEdit.setText(str(z))

    def fill_tab(self):
        """
        Je nachdem, welches Muster gewählt wurde, werden die seitliche Tabelle und die Tabelle über der Spielfläche mit
        Zahlen versehen, welche zur Beschriftung dienen.
        """
        if (self.level == "Medium"):
            # filling table left
            list_bes = [[2,0,0,0,0,0,0,0],
                         [2,3,0,0,0,0,0,0],
                         [1,2,4,0,0,0,0,0],
                         [9,0,0,0,0,0,0,0],
                         [6,0,0,0,0,0,0,0],
                         [6,0,0,0,0,0,0,0],
                         [6,0,0,0,0,0,0,0],
                         [1,1,3,0,0,0,0,0],
                         [2,0,0,0,0,0,0,0],
                         [2,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0]]
            for j in range(15):
                for i in range(8):
                    list = [j, i]
                    self.led = QtGui.QLineEdit(str(list_bes[j][i]))
                    self.view.tableWidget_3.setItem(j,i,QtGui.QTableWidgetItem())
                    self.view.tableWidget_3.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))


            # filling table up
            list_bes2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,5,0,0,0,7,4,3,0,0,0,0,0],
                        [1,2,2,1,5,5,5,1,2,3,0,0,0,0,0]]
            for j in range(8):
                for i in range(15):
                    list = [j, i]
                    self.led = QtGui.QLineEdit(str(list_bes2[j][i]))
                    self.view.tableWidget_4.setItem(j,i,QtGui.QTableWidgetItem())
                    self.view.tableWidget_4.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
                 #   self.tableWidget_3.item(j,i).setText("xy")

        elif (self.level == "Easy"):
            # filling table left
            list_bes = [[0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [1,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0]]
            for j in range(15):
                for i in range(8):
                    list = [j, i]
                    self.led = QtGui.QLineEdit(str(list_bes[j][i]))
                    self.view.tableWidget_3.setItem(j,i,QtGui.QTableWidgetItem())
                    self.view.tableWidget_3.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
                 #   self.tableWidget_3.item(j,i).setText("xy")

            # filling table up
            list_bes2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]]
            for j in range(8):
                for i in range(15):
                    list = [j, i]
                    self.led = QtGui.QLineEdit(str(list_bes2[j][i]))
                    self.view.tableWidget_4.setItem(j,i,QtGui.QTableWidgetItem())
                    self.view.tableWidget_4.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))

                 #   self.tableWidget_3.item(j,i).setText("xy")
        elif (self.level == "Hard"):
            # filling table left
            list_bes = [[9,0,0,0,0,0,0,0],
                         [2,5,2,0,0,0,0,0],
                         [4,3,4,0,0,0,0,0],
                         [6,1,6,0,0,0,0,0],
                         [3,3,3,0,0,0,0,0],
                         [3,3,3,0,0,0,0,0],
                         [3,3,3,0,0,0,0,0],
                         [15,0,0,0,0,0,0,0],
                         [15,0,0,0,0,0,0,0],
                         [2,2,0,0,0,0,0,0],
                         [3,3,0,0,0,0,0,0],
                         [4,4,0,0,0,0,0,0],
                         [4,4,0,0,0,0,0,0],
                         [11,0,0,0,0,0,0,0],
                         [9,0,0,0,0,0,0,0]]
            for j in range(15):
                for i in range(8):
                    list = [j, i]
                    self.led = QtGui.QLineEdit(str(list_bes[j][i]))
                    self.view.tableWidget_3.setItem(j,i,QtGui.QTableWidgetItem())
                    self.view.tableWidget_3.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
                 #   self.tableWidget_3.item(j,i).setText("xy")

            # filling table up
            list_bes2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,2,0,0,   0,2,1,0,0,0,0],
                        [0,0,0,4,2,1,3,0,   3,1,2,4,0,0,0],
                        [0,0,8,2,2,2,5,9,   5,2,2,2,8,0,0],
                        [9,11,4,4,3,2,2,2,  2,2,3,4,4,11,9]]
            for j in range(8):
                for i in range(15):
                    list = [j, i]
                    self.led = QtGui.QLineEdit(str(list_bes2[j][i]))
                    self.view.tableWidget_4.setItem(j,i,QtGui.QTableWidgetItem())
                    self.view.tableWidget_4.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))

                 #   self.tableWidget_3.item(j,i).setText("xy")
