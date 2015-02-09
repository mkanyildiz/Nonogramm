from PyQt4.examples.dialogs.standarddialogs import Dialog

__author__ = 'mwech'

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from src.VC.MyPopup import MyPopup

"""
@author: Kanyildiz
@date: 09.02.2015
"""

class MyView(QtGui.QWidget):
    """
    MyView
    :param MyView: QWidget
    """
    liste = []
    level = []
    erg = []


    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        MyView.liste = []
        MyView.level = []
        MyView.erg = []

    def setupUi(self, Dialog):
        """

        :param Dialog:
        :return setupUi()
        """
        try:
            _fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            def _fromUtf8(s):
                return s
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(925, 828)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(_fromUtf8("background-color:#566C87\n"
""))
        self.tableWidget_2 = QtGui.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(90, 280, 451, 451))
        self.tableWidget_2.setStyleSheet(_fromUtf8("background-color:white;\n"
"border-width:10px;"))
        self.tableWidget_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setRowCount(15)
        self.tableWidget_2.setColumnCount(15)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_2.setItem(0, 0, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.NoEditTriggers
        self.tableWidget_3 = QtGui.QTableWidget(Dialog)
        self.tableWidget_3.setGeometry(QtCore.QRect(550, 280, 241, 451))
        self.tableWidget_3.setStyleSheet(_fromUtf8("background-color:lightgrey;"))
        self.tableWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setAutoScroll(True)
        self.tableWidget_3.setRowCount(15)
        self.tableWidget_3.setColumnCount(8)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.NoEditTriggers
        self.tableWidget_4 = QtGui.QTableWidget(Dialog)
        self.tableWidget_4.setGeometry(QtCore.QRect(90, 30, 451, 241))
        self.tableWidget_4.setStyleSheet(_fromUtf8("background-color:lightgrey;\n"
"border: 10px;\n"
""))
        self.tableWidget_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setAutoScroll(True)
        self.tableWidget_4.setRowCount(8)
        self.tableWidget_4.setColumnCount(15)
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.horizontalHeader().setVisible(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.NoEditTriggers
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 770, 131, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:white;\n"
"border-radius:10px;"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 769, 111, 31))
        self.label.setStyleSheet(_fromUtf8("font-size: 15px"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 770, 91, 31))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:#4099ff;\n"
"border-radius:10px;\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 770, 81, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:#334E6e;\n"
"border-radius:10px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(510, 770, 101, 31))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:white\n"
""))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """

        :param Dialog:
        :return retranslateUi()
        """
        try:
            _encoding = QtGui.QApplication.UnicodeUTF8
            def _translate(context, text, disambig):
                return QtGui.QApplication.translate(context, text, disambig, _encoding)
        except AttributeError:
            def _translate(context, text, disambig):
                return QtGui.QApplication.translate(context, text, disambig)
        Dialog.setWindowTitle(_translate("Dialog", "NONOGRAMM", None))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setText(_translate("Dialog", "150", None))
        self.label.setText(_translate("Dialog", "Felder offen:", None))
        self.pushButton.setText(_translate("Dialog", "Lösung", None))
        self.pushButton_2.setText(_translate("Dialog", "Neustart", None))
        self.comboBox.setItemText(0, _translate("Dialog", "Easy", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Medium", None))
        self.comboBox.setItemText(2, _translate("Dialog", "Hard", None))


        self.fill_tab()
        self.neustart()

        self.pushButton_2.clicked.connect(self.neustart)
        self.tableWidget_2.cellClicked.connect(self.cell_was_clicked)
        self.pushButton.clicked.connect(self.loesung)

    def fill_tab(self):

        """
        fill_tab
        :rtype : je nachdem welcher muster gewählt wurde werden die seitlichentabellen bzw. die tabelle über der Spielfläche mit zahlen versehen die zur beschriftung dienen
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
                    self.tableWidget_3.setItem(j,i,QtGui.QTableWidgetItem())
                    self.tableWidget_3.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
                 #   self.tableWidget_3.item(j,i).setText("xy")

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
                    self.tableWidget_4.setItem(j,i,QtGui.QTableWidgetItem())
                    self.tableWidget_4.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
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
                    self.tableWidget_3.setItem(j,i,QtGui.QTableWidgetItem())
                    self.tableWidget_3.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
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
                    self.tableWidget_4.setItem(j,i,QtGui.QTableWidgetItem())
                    self.tableWidget_4.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
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
                    self.tableWidget_3.setItem(j,i,QtGui.QTableWidgetItem())
                    self.tableWidget_3.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
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
                    self.tableWidget_4.setItem(j,i,QtGui.QTableWidgetItem())
                    self.tableWidget_4.setItem(j, i, QtGui.QTableWidgetItem(self.led.text()))
                 #   self.tableWidget_3.item(j,i).setText("xy")

    def neustart(self):
        """
        neustart()
        :rtype : alle felder werden gelöscht und die spielfläche wird wieder ins anfangs stadium zurück versetzt
        """
        for j in range(15):
            for i in range(15):
                list = [j, i]
                self.tableWidget_2.setItem(j,i,QtGui.QTableWidgetItem())
                self.tableWidget_2.item(j,i).setBackground(QtGui.QColor('white'))
        self.level = self.comboBox.currentText()

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
            #for z in range(len(self.erg)):
            #    self.cell_clicked(self.erg[z][0], self.erg[z][1])

        elif self.level == "Easy":
            self.erg = [[7,7]]
          #  for z in range(len(self.erg)):
          #     self.cell_clicked(self.erg[z][0], self.erg[z][1])

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

    def cell_was_clicked(self, row, column):
        """

        cell_was_clicked(row,column)

        :rtype : die methode füllt eine zelle mit schwarzer farbe falls eine zelle angeklickt wird. Desweiteren wir die zelle wieder weiß angemalt falls diese bereits geklickt wurde
        :param row: die zeilen anzahl wo sich die geklickte zelle befindet
        :param column: die spalten anzahl wo sich die geklickte zelle befindet
        """
        list = [row, column]
        self.cells_left()
        if list in self.liste:
            self.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
            item = self.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('white'))
            a = self.liste.index(list)
            del self.liste[a]
        else:
            self.liste.append([row, column])
            self.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
            item = self.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('black'))

        if self.liste == self.erg:
            self.w = MyPopup()
            self.w.setGeometry(QRect(100, 100, 400, 200))
            self.w.show()
            self.neustart()
            self.liste = []


    def cell_clicked(self, row, column):
        """

        cell_clicked(row,column)

        :rtype : diese methode ähnelt der cell_was_clicked methode. Der einzige unterschied liegt darin, dass wir hier nicht überprüfen ob die zelle bereits geklickt wurde da dies beim lösung anzeigen vom nachteil ist
        :param row: die zeilen anzahl wo sich die geklickte zelle befindet
        :param column: die spalten anzahl wo sich die geklickte zelle befindet
        """
        list = [row, column]
        self.liste.append([row, column])
        self.tableWidget_2.setItem(list[0], list[1], QtGui.QTableWidgetItem())
        item = self.tableWidget_2.item(list[0], list[1]).setBackground(QtGui.QColor('black'))

    def loesung(self):
        """
        loesung()
        :rtype : hier wird die lösung ausgegeben
        """
        self.level = self.comboBox.currentText()
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
            #for z in range(len(self.erg)):
            #    self.cell_clicked(self.erg[z][0], self.erg[z][1])

        elif self.level == "Easy":
            self.erg = [[7,7]]
          #  for z in range(len(self.erg)):
          #     self.cell_clicked(self.erg[z][0], self.erg[z][1])

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
        i = len(self.erg)
        z=0
        for self.erg in self.liste:
            z += 1
            print(self.liste)
            if self.erg[z] not in self.liste:
                i += 1
            if self.erg[z] in self.liste:
                i -= 1

        self.lineEdit.setText(str(i))


