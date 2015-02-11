from random import randint
from PyQt4 import QtGui
from PyQt4.QtCore import QRect
from src.MVC.MyPopup import Popup
from jinja2._compat import izip
from pip._vendor.requests.packages.urllib3.connectionpool import xrange
from pip.backwardcompat import reduce


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
    erg = []
    erg2 = []
    liste_right = []
    liste_top = []
    def setView(self, MyView):
        """
        Eine neue View erstellen
        :param MyView: die View Klasse
        """
        self.view = MyView
        self.level = ""
        self.erg = []
        self.liste_right = []
        self.liste_top = []
        self.erg2 = []



    def neustart(self):
        #liste als zwischenspiecher für die beschriftung

        """
        Mit dieser Methode werden alle im Array gespeicherten Felder gelöscht und die Spielfläche wird wieder ins
        Anfangsstadium zurückversetzt, sprich in weißer Farbe.
        """
        self.erg = []
        zaehler = 0
        self.erg2 = []
        self.liste_right = []
        self.liste_top = []
        for j in range(15):
            for i in range(15):
                list = [j, i]
                self.view.tableWidget_2.setItem(j,i,QtGui.QTableWidgetItem())
                self.view.tableWidget_2.item(j,i).setBackground(QtGui.QColor('white'))
        self.level = self.view.comboBox.currentText()

        if self.level == "Medium":
            for j in range(15):
                randomnum1 = 0
                randomnum2 = 0
                nb_list = []
                spalte = []
                for i in range(3):

                    if i == 0:
                        randomnum1 = randint(0,5)
                    else:
                        randomnum1 = randint(randomnum2+1,randomnum2+3)
                    if i == 0:
                        randomnum2 = randint(randomnum1+1, randomnum1+4)
                    else:
                        randomnum2 = randint(randomnum1+1,randomnum1+5)

                    if randomnum1 >= 14:
                        randomnum1 = 14
                        break
                    elif randomnum2 >= 14:
                        randomnum2 = 14
                        break



                    for z in range(randomnum1,randomnum2):
                        self.erg.append([j,z])
                        self.erg2.append([z,j])
                    nb_list.append(randomnum2-randomnum1)
                self.liste_right.append(nb_list)

            #Here we are refractoring the erg array so that we hava a two dimensional array which contains
            #each column in a seperate array. We will use this array later on to count the fields in the actual column
            result = []
            for a in range(14):
                spalte = []
                for item in self.erg2:
                    if (item[0] == a):
                        spalte.append(item)
                result.append(spalte)
                #if item[0][1]+1 in self.erg2[]:
            #result.append(spalte)
            #print(result)

            #Now we hav to check if the columns are seperated by white cells if so then we have to set the
            #counter to 0 and start to count again
            zaehler = 0
            zwischen=[]
            for y in range(len(result)):
                for x in range(len(result[y])):
                    if x != len(result[y])-1 and y != len(result)-1:
                        if result[y][x+1][1] != result[y][x][1]+1:
                            zaehler = 1

                        else:
                            zaehler+=1

                    zwischen.append(zaehler)
                self.liste_top.append(zwischen)

        elif self.level == "Easy":
            for j in range(15):
                randomnum1 = 0
                randomnum2 = 0
                nb_list = []
                spalte = []
                for i in range(3):

                    if i == 0:
                        randomnum1 = randint(0,1)
                    else:
                        randomnum1 = randint(randomnum2+1,randomnum2+2)
                    if i == 0:
                        randomnum2 = randint(randomnum1+6, randomnum1+10)
                    else:
                        randomnum2 = randint(randomnum1+3,randomnum1+5)

                    if randomnum1 >= 14:
                        randomnum1 = 14
                        break
                    elif randomnum2 >= 14:
                        randomnum2 = 14
                        break


                    for z in range(randomnum1,randomnum2):
                        self.erg.append([j,z])
                        self.erg2.append([z,j])
                    nb_list.append(randomnum2-randomnum1)
                self.liste_right.append(nb_list)

            #Here we are refractoring the erg array so that we hava a two dimensional array which contains
            #each column in a seperate array. We will use this array later on to count the fields in the actual column
            result = []
            for a in range(14):
                spalte = []
                for item in self.erg2:
                    if (item[0] == a):
                        spalte.append(item)
                result.append(spalte)
                #if item[0][1]+1 in self.erg2[]:
            #result.append(spalte)
            #print(result)

            #Now we hav to check if the columns are seperated by white cells if so then we have to set the
            #counter to 0 and start to count again
            zaehler = 0
            zwischen=[]
            for y in range(len(result)):
                for x in range(len(result[y])):
                    if x != len(result[y])-1 and y != len(result)-1:
                        if result[y][x+1][1] != result[y][x][1]+1:
                            zaehler = 1

                        else:
                            zaehler+=1

                    zwischen.append(zaehler)
                self.liste_top.append(zwischen)

        elif self.level == "Hard":
            for j in range(15):
                randomnum1 = 0
                randomnum2 = 0
                nb_list = []
                spalte = []

                for i in range(3):

                    if i == 0:
                        randomnum1 = randint(0,5)
                    else:
                        randomnum1 = randint(randomnum2+1,randomnum2+2)
                    if i == 0:
                        randomnum2 = randint(randomnum1+1, randomnum1+2)
                    else:
                        randomnum2 = randint(randomnum1+1,randomnum1+2)

                    if randomnum1 >= 14:
                        randomnum1 = 14
                        break
                    elif randomnum2 >= 14:
                        randomnum2 = 14
                        break



                    for z in range(randomnum1,randomnum2):
                        self.erg.append([j,z])
                        self.erg2.append([z,j])
                    nb_list.append(randomnum2-randomnum1)
                self.liste_right.append(nb_list)


            #Here we are refractoring the erg array so that we hava a two dimensional array which contains
            #each column in a seperate array. We will use this array later on to count the fields in the actual column
            result = []
            for a in range(14):
                spalte = []
                for item in self.erg2:
                    if (item[0] == a):
                        spalte.append(item)
                result.append(spalte)
                #if item[0][1]+1 in self.erg2[]:
            #result.append(spalte)
            #print(result)

            #Now we hav to check if the columns are seperated by white cells if so then we have to set the
            #counter to 0 and start to count again
            zaehler = 0
            zwischen=[]
            for y in range(len(result)):
                for x in range(len(result[y])):
                    if x != len(result[y])-1 and y != len(result)-1:
                        if result[y][x+1][1] != result[y][x][1]+1:
                            zaehler = 1

                        else:
                            zaehler+=1

                    zwischen.append(zaehler)
                self.liste_top.append(zwischen)

        list = []


        for j in range(len(self.liste_right)):
            length_list = len(self.liste_right[j])
            null_count = 8-length_list
            print(self.liste_right[j])
            print(null_count)
            for x in range(null_count):
                self.liste_right[j].append(0)


        print(self.liste_right)
        print("Hallo!")

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
        if (self.level == "Medium" or self.level == "Easy" or self.level == "Hard"):
            # filling table left

            for j in range(15):
                for i in range(8):
                    list = [j, i]
                    self.led = QtGui.QLineEdit(str(self.liste_right[j][i]))
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



