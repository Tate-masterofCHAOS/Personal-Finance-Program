import os
import tkinter as tk
from slct_prfl import Slct

import csv

class Baimenu:
    def __init__(self, root):

        file_path = Slct().selected_file
        print(f"Selected file path: {file_path}")

        # Proceed with using the file path
        if file_path:
            with open(file_path, 'r') as file:
                data = csv.reader(file)
                print(data)
        # ROWS 3-4

        self.root = root  # Use the passed root window
        self.root.title('Income and Expense Tracking')

        # Clear any existing widgets in the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Example: Add a label to the existing window
        tk.Label(self.root, text='Income and Expense Tracking').pack(pady=10)

        # Example: Add a button to go back to the main menu
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=10)

        # Create a Listbox to display CSV file names
        income = tk.Listbox(self.root, height=10, width=50)
        income.pack(pady=5)

        # Populate the Listbox with CSV file names
        #for item in csv file row 3:

        #    item.replace('_', '   ')
        #    income.insert(tk.END, item.split('_'))

        # Create a button to go back to the main menu

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)
    
    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu
