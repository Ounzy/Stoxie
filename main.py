from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from backend.yfinance.markets.markets import *
from backend.yfinance.markets.markets_objects import *
from backend.yfinance.lookup.lookup import *

import sys


""" class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(getMarketEurope)
   
        self.setCentralWidget(button)

        self.setFixedSize(QSize(400,300))

    def the_button_was_clicked(self):
        print("cklicked!")

        

        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec() """

#getMarketEurope()
lookup()