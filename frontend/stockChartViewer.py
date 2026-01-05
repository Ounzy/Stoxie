import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import mplcursors  # Import für die Interaktivität

class ChartCanvas(FigureCanvas):
    def __init__(self):
        # Initialisierung der Figur
        self.fig, self.ax = plt.subplots(tight_layout=True)
        super().__init__(self.fig)

    def plot_stock(self, df):
        self.ax.clear()
        
        # 1. Die Linie zeichnen und in einer Variable 'line' speichern
        line, = self.ax.plot(df.index, df['Close'], color='#0078D4', linewidth=2)
        
        # 2. Interaktiven Cursor hinzufügen
        cursor = mplcursors.cursor(line, hover=True) # hover=True zeigt es beim Drüberfahren
        
        @cursor.connect("add")
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