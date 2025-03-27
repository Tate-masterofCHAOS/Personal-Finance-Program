import os
import tkinter as tk
from slct_prfl import Slct

import pandas as pd

class Baimenu:
    def __init__(self):

        file_path = Slct()
        # ROWS 3-4

        # Create a new tkinter window to select a CSV file
        self.root = tk.Tk()
        self.root.title('Title')

        tk.Label(self.root, text='Select a CSV File:').pack(pady=5)

        # Create a Listbox to display CSV file names
        income = tk.Listbox(self.root, height=10, width=50)
        income.pack(pady=5)

        # Populate the Listbox with CSV file names
        #for item in csv file row 3:

        #    item.replace('_', '   ')
        #    income.insert(tk.END, item.split('_'))

        # Create a button to go back to the main menu
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=10)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)
    
    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu
