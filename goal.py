import os
import tkinter as tk
from slct_prfl import Charts  # Import the Charts class from slct_prfl.py

import pandas as pd

class Baimenu:
    def __init__(self):

        file_path = Charts()
        # ROW 1 ITEM 1 IN A LIST ONLY, COLUMN 2

        # Create a new tkinter window to select a CSV file
        self.root = tk.Tk()
        self.root.title('Title')

        txt = CSV file row 1 col 2

        tk.Label(self.root, text=txt).pack(pady=5)

        # Create a button to go back to the main menu
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=10)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)
    
    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu
