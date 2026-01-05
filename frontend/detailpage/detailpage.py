from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
import yfinance as yf
from backend.yfinance.ticker.tickerInfo import *
from frontend.stockChartViewer import *
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor


class DetailPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)


        self.header_widget = QWidget()
        self.header_widget.setObjectName("header")

        self.chartWidget = QWidget()

        self.chart = ChartCanvas(self.chartWidget)

        chartContainerLayout = QVBoxLayout(self.chartWidget)
        chartContainerLayout.setContentsMargins(0, 0, 0, 0)
        chartContainerLayout.addWidget(self.chart)

        

        self.pageLayout = QVBoxLayout(self)
        self.headerLayout = QHBoxLayout(self.header_widget)
        self.chartLayout = QHBoxLayout(self.chartWidget)

        self.tickerName = QLabel()
        self.shortName = QLabel()
        self.choseHistoryPeriod = QComboBox(self.chartWidget)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 150))
        self.choseHistoryPeriod.setGraphicsEffect(shadow)

        # 2. Mauszeiger ändern
        self.choseHistoryPeriod.setCursor(Qt.CursorShape.PointingHandCursor)
        
        historyList = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']

        for i in historyList:
            self.choseHistoryPeriod.addItem(i)

        self.choseHistoryPeriod.setFixedWidth(80)
        self.choseHistoryPeriod.raise_()
        
        self.choseHistoryPeriod.currentTextChanged.connect(self.changeHistoryPeriod)

        self.headerLayout.addWidget(self.tickerName)        #header
        self.headerLayout.addStretch()                      
        self.headerLayout.addWidget(self.shortName)

        self.chart.resize(self.chartWidget.size())                                              #Verschieben der Historycombobox
        x_center = (self.chartWidget.width() // 2) - (self.choseHistoryPeriod.width() // 2)
        y_pos = 20 
        self.choseHistoryPeriod.move(x_center, y_pos)

        

        self.pageLayout.addWidget(self.header_widget)
        self.pageLayout.addWidget(self.chartWidget)

        
        
        self.pageLayout.addStretch()

        self.setLayout(self.pageLayout)
    
    tickerArg = str
    def setData(self, t):
        self.tickerName.setText(t)
        self.getTicker(t)
        
        

    def getTicker(self, t):
        self.tickerInput = t                                #   'MSFT'
        self.ticker = yf.Ticker(t)                           #   whole ticker
        self.getTickerInfo(self.ticker)
        self.update_stock_data(self.ticker, '3mo')
        #print(tickerInfo)

    tickerInfo = {}
    def getTickerInfo(self, t):
        #tickerInfo = t.info.where(tickerInfo.notnull(), None)
        tickerInfoClean = TickerInfo.model_validate(t.info)
        #print(tickerInfoClean)
        self.shortName.setText(tickerInfoClean.longName)


    def getTickerHistory(self, ticker, period):
        return ticker.history(period=period, interval = '1d')

    def update_stock_data(self, ticker, period):
        tickerHistory = self.getTickerHistory(ticker, period)
        #if (period == '1d'):
        print(tickerHistory)
        self.chart.plot_stock(tickerHistory)

    def changeHistoryPeriod(self):
        self.update_stock_data(self.ticker, self.choseHistoryPeriod.currentText())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        
        self.chart.resize(self.chartWidget.size())
        
        x_center = (self.chartWidget.width() // 2) - (self.choseHistoryPeriod.width() // 2)
        
        y_pos = 20 
        
        self.choseHistoryPeriod.move(x_center, y_pos)

      