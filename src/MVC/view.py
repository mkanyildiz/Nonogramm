from PyQt4.examples.dialogs.standarddialogs import Dialog
from src.MVC.controller import MyController
from src.MVC.model import MyModel
from PyQt4 import QtCore, QtGui

"""
@author: Muhammed Kanyildiz, Maximilian Wech
@version: 20150209
@description: In dieser Klasse wird das GUI aufgebaut. Dies bedeutet, dass die Widgets, Buttons, Labels, etc. erstellt
              und initialisiert werden.
"""

class MyView(QtGui.QWidget, MyModel, MyController):
    """
    MyView
    :param MyView: QWidget

    Attributes:
    liste   Array für das Speichern der vom Benutzer ausgewählten Felder.
    level   Die Spielschwierigkeit; Anzahl der vorgegebenen Zahlen
    erg     In dieses Array werden die richtigen Felder (Lösungsfelder) gespeichert.
    m       Instanz der Model Klasse
    c       Instanz der Controller Klasse
    """
    liste = []
    level = []
    erg = []
    m = None
    c = None

    def __init__(self, MyModel, MyController):
        """
        Konstruktor
        """
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        MyView.liste = []
        MyView.level = []
        MyView.erg = []

    def setupUi(self, Dialog):
     """
        Diese Methode erstellt und konfiguriert die Elemente des GUI's.
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
        Es werden die textuellen Einstellungen der geänderten Komponenten umgesetzt.
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


