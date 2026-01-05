# theme.py

class Theme:
    # Hauptfarben
    MODES = {
        "dark": {
            "BACKGROUND": "#121212",
            "CARD_BG": "#1E1E1E",
            "TEXT_MAIN": "#E0E0E0",
            "PRIMARY": "#0078D4"
        },
        "light": {
            "BACKGROUND": "#F5F5F5",
            "CARD_BG": "#FFFFFF",
            "TEXT_MAIN": "#202020",
            "PRIMARY": "#005A9E"
        }
    }    
    
    # Statusfarben
    POSITIVE = "#26A69A"     
    NEGATIVE = "#EF5350"     

    currentMode = "light"

    @classmethod
    def get_stylesheet(cls):
        colors = cls.MODES[cls.currentMode]
        return f"""
            QWidget {{
                background-color: {colors['BACKGROUND']};
                color: {colors['TEXT_MAIN']};
                font-family: 'Segoe UI', Arial;
            }}

            QWidget#header {{
                background-color: {colors['CARD_BG']};
                border-bottom: 1px solid #333333;
                padding: 10px;
            }}
            
            QPushButton {{
                background-color: {colors['PRIMARY']};
                border-radius: 4px;
                padding: 8px;
                color: white;
            }}
        """