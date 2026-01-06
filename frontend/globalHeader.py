from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget
from PyQt6.QtCore import Qt, QPoint
from backend.yfinance.lookup.lookup import *

class GlobalHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("globalHeader")
        self.setFixedHeight(60)
        
        # Hauptlayout für den Header
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(20, 0, 20, 0)
        
        # Logo oder App-Name
        self.logoLabel = QLabel("STOXIE")
        self.logoLabel.setStyleSheet("font-size: 18px; font-weight: bold; color: #0078D4;")
        
        # Suchleiste (damit sie überall verfügbar ist)
        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Aktie suchen...")
        self.searchBar.textChanged.connect(self.textChanged)
        self.searchBar.setFixedWidth(250)

        self.suggestionList = QListWidget(self.window())
        self.suggestionList.setParent(self.window())
        self.suggestionList.setFixedWidth(self.searchBar.width()) # Gleiche Breite wie SearchBar
        self.suggestionList.hide()
        self.suggestionList.setWindowFlags(Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint)
        self.suggestionList.itemClicked.connect(self.hideSuggestionList)
        # Widgets zum Layout hinzufügen
        self.layout.addWidget(self.logoLabel)
        self.layout.addStretch() # Schiebt die Suche nach rechts
        self.layout.addWidget(self.searchBar)


        lookupInput = {}
    def textChanged(self, s):
        if (len(s) > 1 ):
            self.suggestionList.clear()
            lookupInput = lookup(s)
            if lookupInput != False: 
                for key, data in lookupInput.items():
                    self.suggestionList.addItem(f"{key} ({data.shortName})" )
                    pos = self.searchBar.pos()
                self.suggestionList.move(pos.x(), pos.y() + self.searchBar.height())
                
                self.update_suggestion_pos()
                self.suggestionList.show()
                self.suggestionList.raise_() # Sicherstellen, dass sie oben liegt
            else:
                self.suggestionList.hide()
        else:
            self.suggestionList.hide()
            return
        
    def update_suggestion_pos(self):
        point = self.searchBar.mapToGlobal(QPoint(0, self.searchBar.height()))
        self.suggestionList.move(point)
        self.suggestionList.setFixedWidth(self.searchBar.width())

    def hideSuggestionList(self):
        self.suggestionList.hide()
        self.suggestionList.clear()
        self.searchBar.clear()
                
    #def setTitle(self, title):
    #    """Erlaubt es, den Titel von außen zu ändern (z.B. Aktiensymbol)"""
    #    self.logoLabel.setText(f"STOXIE | {title}")