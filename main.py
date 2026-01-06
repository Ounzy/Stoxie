from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QListWidget, QVBoxLayout, QStackedWidget
from backend.yfinance.markets.markets import *
from backend.yfinance.markets.markets_objects import *
from backend.yfinance.lookup.lookup import *
from frontend.searchPage.searchPage import *
from frontend.detailpage.detailpage import *
from frontend.globalHeader import *
from frontend.globalHeader import *
from theme import *

import sys




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.mainLayout = QVBoxLayout(self.centralWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        
        self.header = GlobalHeader()
        self.mainLayout.addWidget(self.header)

        self.stackedWidget = QStackedWidget()

        self.searchPage = SearchPage()
        self.detailPage = DetailPage()
        
        self.stackedWidget.addWidget(self.searchPage)
        self.stackedWidget.addWidget(self.detailPage)
        self.mainLayout.addWidget(self.stackedWidget)
        
        self.stackedWidget.setCurrentIndex(0)
        self.setMinimumSize(QSize(400, 300))

        self.searchPage.screener.itemClicked.connect(self.onTickerSelected)
        self.header.suggestionList.itemClicked.connect(self.onTickerSelected)

    def onTickerSelected(self, item):               #when searchpage qlistwidget asset selected
        ticker = item.text().split(" ")[0]
        self.detailPage.setData(ticker)
        self.stackedWidget.setCurrentIndex(1)



def toggle_theme(self):
    if Theme.current_mode == "dark":
        Theme.current_mode = "light"
    else:
        Theme.current_mode = "dark"
    
    from PyQt6.QtWidgets import QApplication
    QApplication.instance().setStyleSheet(Theme.get_stylesheet())
    
    print(f"Modus gewechselt zu: {Theme.current_mode}")



#window = MainWindow()
#window.show()

#app.exec() 

#getMarketEurope()
#lookup()

def main():
    app = QApplication(sys.argv)
    
    # Hier wenden wir den Style global an
    app.setStyleSheet(Theme.get_stylesheet())
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

