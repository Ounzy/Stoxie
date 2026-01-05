from PyQt6.QtWidgets import QListWidget, QWidget, QVBoxLayout
import yfinance as yf

class DetailPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.pageLayout = QVBoxLayout()
        self.List = QListWidget()
        self.pageLayout.addWidget(self.List)

        self.setLayout(self.pageLayout)
    
    tickerArg = str
    def setData(self, t):
        self.List.addItem(t)
        self.getTicker(t)
        
        

    def getTicker(self, t):
        ticker = yf.Ticker(t)
        tickerInfo = ticker.info
        print(ticker.history(period='1mo'))
        #print(tickerInfo)