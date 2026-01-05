import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


class ChartCanvas(FigureCanvas):

    def __init__(self, parent=None): # Hier 'parent' hinzufügen
        self.fig, self.ax = plt.subplots(tight_layout=True)
        super().__init__(self.fig)
        self.setParent(parent) # Setzt das Widget in den Container


    def plot_stock(self, df):
        self.ax.clear()
        
        if hasattr(self, 'interactive_cursor') and self.interactive_cursor is not None:
            try:
                self.interactive_cursor.remove()
            except Exception:
                pass # Falls das Entfernen fehlschlägt, machen wir trotzdem weiter
            self.interactive_cursor = None

        if len(df) < 10:
        # Zeichnet vertikale Linien von Low zu High für jeden Zeitpunkt (Index)
        # vlines(x, ymin, ymax)
            self.ax.vlines(df.index, df['Low'], df['High'], 
                       color='#0078D4', linewidth=2, label='High-Low Range')
            
            self.ax.vlines(df.index, df['Open'], df['Close'],
                        color='black', linewidth=10, label='Open and Close')
        
        # Optional: Einen kleinen Punkt für den Close-Preis auf der Linie setzen
        #    self.ax.scatter(df.index, df['Close'], color='white', s=20, zorder=3, label='Close')
        
            self.ax.legend(facecolor='#1E1E1E', labelcolor='white', edgecolor='none')
        else:
            # Standard-Linienchart für mehr als 10 Punkte
            self.ax.plot(df.index, df['Close'], color='#0078D4', linewidth=2)
        
        # 2. Interaktiven Cursor hinzufügen
        import mplcursors
        self.interactive_cursor = mplcursors.cursor(self.ax.get_lines() + list(self.ax.collections), hover=True) # hover=True zeigt es beim Drüberfahren
        
        @self.interactive_cursor.connect("add")
        def _(sel):
            # sel.target[0] ist die X-Achse (Datum), sel.target[1] ist die Y-Achse (Preis)
            # Wir formatieren den Preis auf 2 Nachkommastellen
            price = sel.target[1]
            sel.annotation.set_text(f"{price:.2f} €")
            
            # Styling des Tooltips (Weißer Hintergrund, schwarze Schrift)
            sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9, boxstyle="round")
            sel.annotation.set_fontsize(10)

        # 3. Design-Anpassungen (Dark Mode)
        self.ax.set_facecolor('#1E1E1E')
        self.fig.patch.set_facecolor('#121212')
        self.ax.tick_params(colors='white')
        self.ax.grid(True, linestyle='--', alpha=0.2, color='gray')
        
        # Datum schräg stellen für bessere Lesbarkeit
        self.fig.autofmt_xdate()
        
        self.draw()