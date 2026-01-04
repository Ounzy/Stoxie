from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QListWidget, QVBoxLayout
from backend.yfinance.markets.markets import *
from backend.yfinance.markets.markets_objects import *
from backend.yfinance.lookup.lookup import *
import sys

class SearchPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

           #window title is declared here but should be in the main.py probably 
                                        #also MainWindow should be in the main.py

        self.pageLayout = QVBoxLayout()

   

        screenerInput = QLineEdit()
        screenerInput.setPlaceholderText("Name of your asset")
        screenerInput.textChanged.connect(self.textChanged)

        self.screener = QListWidget()
        #self.screener.itemClicked.connect(self.clickedAsset)
        

        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(getMarketEurope) # still have to change that

        self.pageLayout.addWidget(screenerInput)
        self.pageLayout.addWidget(self.screener)
        self.pageLayout.addWidget(button)
   
        self.setLayout(self.pageLayout)

        lookupInput = {}
    def textChanged(self, s):
        if (len(s) > 1 ):
            self.screener.clear()
            lookupInput = lookup(s)
            if lookupInput != False: 
                for key, data in lookupInput.items():
                    self.screener.addItem(f"{key} ({data.shortName})" )
            else: 
                self.screener.addItem("No results")
        else: 
            return
        #print(lookupInput)

    def the_button_was_clicked(self):
        print("cklicked!")

    """ def clickedAsset(self, s):
        tickerArray = s.text().split(" ")
        ticker = tickerArray[0]
        print(ticker) """