from src.VC.view import MyView

__author__ = 'mwech'

class MyController():

    def __init__(self):
        self.view = MyView()

    def main(self):
        self.view.show()