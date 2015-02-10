from src.MVC.view import MyView
from src.MVC.model import MyModel

"""
@author: Muhammed Kanyildiz, Maximilian Wech
@version: 20150209
@description: Reaktionen auf Eingaben des Benutzers durchführen.
"""

class MyController(MyModel):
    """
    Attributes:
    model   Instanz der Model Klasse
    view    Instanz der View Klasse
    """
    model = None
    view = None

    def __init__(self, m):
        """
        Konstruktor
        """
        self.model = m
        self.view = MyView(self.model, self)
        self.model.setView(self.view)

    def main(self):
        """
        Anzeige des GUI's mittels der show() Methode, Ausführung von Methoden um den Spielstart zu gewährleisten;
        Reaktionen auf Button / Spielfeld Klicks --> Reaktion auf Benutzereingaben.
        """
        self.view.show()
        self.model.fill_tab()
        self.model.neustart()
        self.view.pushButton_2.clicked.connect(self.model.neustart)
        self.view.tableWidget_2.cellClicked.connect(self.model.cell_was_clicked)
        self.view.pushButton.clicked.connect(self.model.loesung)
        level = self.view.comboBox.currentText()
        self.view.comboBox.currentIndexChanged.connect(self.model.neustart)