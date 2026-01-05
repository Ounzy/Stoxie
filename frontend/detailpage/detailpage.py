from PyQt6.QtWidgets import QListWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel
import yfinance as yf
from backend.yfinance.ticker.tickerInfo import *
from frontend.stockChartViewer import *


class DetailPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)


        self.header_widget = QWidget()
        self.header_widget.setObjectName("header")

        self.chart = ChartCanvas()

        self.pageLayout = QVBoxLayout(self)
        self.infoLayoutVertical = QHBoxLayout(self.header_widget)

        self.tickerName = QLabel()
        self.shortName = QLabel()

        self.infoLayoutVertical.addWidget(self.tickerName)

        self.infoLayoutVertical.addStretch()
        
        self.infoLayoutVertical.addWidget(self.shortName)

        self.pageLayout.addWidget(self.header_widget)
        self.pageLayout.addWidget(self.chart)
        
        self.pageLayout.addStretch()

        self.setLayout(self.pageLayout)
    
    tickerArg = str
    def setData(self, t):
        self.tickerName.setText(t)
        self.getTicker(t)
        
        

    def getTicker(self, t):
        ticker = yf.Ticker(t)
        self.getTickerInfo(ticker)
        self.update_stock_data(ticker)
        #print(tickerInfo)

    tickerInfo = {}
    def getTickerInfo(self, t):
        #tickerInfo = t.info.where(tickerInfo.notnull(), None)
        tickerInfoClean = TickerInfo.model_validate(t.info)
        print(tickerInfoClean)
        self.shortName.setText(tickerInfoClean.longName)


    def getTickerHistory(self, ticker, period):
        return ticker.history(period=period, interval = '1d')

    def update_stock_data(self, ticker):
        tickerHistory = self.getTickerHistory(ticker, '3mo')
        self.chart.plot_stock(tickerHistory)