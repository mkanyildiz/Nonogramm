from src.VC.view import MyView

"""
@author: Muhammed Kanyildiz, Maximilian Wech
@version: 20150209
@description: Reaktionen auf Eingaben des Benutzers durchführen.
"""

class MyController():

    def __init__(self):
        """
        Konstruktor
        """
        self.view = MyView()

    def main(self):
        """
        Anzeige des GUI's mittels der show() Methode
        """
        self.view.show()