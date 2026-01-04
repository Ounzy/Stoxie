from PyQt6.QtWidgets import QListWidget, QWidget, QVBoxLayout

class DetailPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.pageLayout = QVBoxLayout()
        self.List = QListWidget()
        self.pageLayout.addWidget(self.List)

        self.setLayout(self.pageLayout)
    
    ticker = str
    def setData(self, t):
        ticker = t
        self.List.addItem(t)