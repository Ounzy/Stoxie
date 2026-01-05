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

            QComboBox {{
                background-color: rgba(40, 40, 40, 230); 
                border: 1px solid #444444;
                border-radius: 8px; 
                padding: 4px 12px;
                color: #E0E0E0;
                font-size: 13px;
                font-weight: 500;
            }}

            QComboBox:hover {{
                border: 1px solid #0078D4; /* Dein Blau-Ton */
                background-color: rgba(50, 50, 50, 250);
            }}

            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left: 0px; 
            }}

            QComboBox QAbstractItemView {{
                background-color: #1e1e1e;
                border: 1px solid #444444;
                border-radius: 8px;
                selection-background-color: #0078D4; /* Blau beim Auswählen */
                color: white;
                outline: none;
                padding: 5px;
            }}

            QComboBox QAbstractItemView::item {{
                min-height: 30px;
                padding-left: 10px;
            }}
                    """
                