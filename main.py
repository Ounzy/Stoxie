from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QListWidget, QVBoxLayout, QStackedWidget
from backend.yfinance.markets.markets import *
from backend.yfinance.markets.markets_objects import *
from backend.yfinance.lookup.lookup import *
from frontend.searchPage.searchPage import *
from frontend.detailpage.detailpage import *
import sys
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.searchPage = SearchPage()
        self.detailPage = DetailPage()
        
        self.stackedWidget.addWidget(self.searchPage)
        self.stackedWidget.addWidget(self.detailPage)
        self.stackedWidget.setCurrentIndex(0)
        self.setMinimumSize(QSize(400, 300))

        self.searchPage.screener.itemClicked.connect(self.onTickerSelected)

    def onTickerSelected(self, item):
        ticker = item.text().split(" ")[0]
        self.detailPage.setData(ticker)
        self.stackedWidget.setCurrentIndex(1)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec() 

#getMarketEurope()
#lookup()