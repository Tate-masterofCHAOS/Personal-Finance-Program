import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from slct_prfl import Slct
import csv
import pandas as pd

class Gmenu:
    def __init__(self, root):
        self.root = root  # Assign the root parameter to self.root
        self.txt = tk.StringVar()
        file_path = Slct().selected_file

        # Initialize an empty list to store all rows
        self.data_rows = []

        # Add UI elements
        tk.Label(self.root, text='Goals').pack(pady=10)
        tk.Label(self.root, text='').pack(pady=10)
        tk.Label(self.root, text='Goal amount:').pack(pady=3)
        tk.Label(self.root, textvariable=self.txt, font=("Helvetica", 12, "bold")).pack(pady=3)
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=20)

        # Proceed with using the file path
        if file_path:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                # Read all rows and store them in self.data_rows
                self.data_rows = [row for row in reader]
            self.display()  # Call the display method to show the data

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def display(self):
        # Display the goal amount from the data
        if self.data_rows:
            self.txt.set(self.data_rows[0][2])  # Set the text variable to the goal amount

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu

class Gset:
    def __init__(self, root):
        txt = tk.StringVar()
        file_path = Slct().selected_file

        # Initialize an empty list to store all rows
        self.data_rows = []

        # Proceed with using the file path
        if file_path:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                # Read all rows and store them in self.data_rows
                self.data_rows = [row for row in reader]
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=10)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)
        def display(self):
            tk.Label(self.root, text='Income and Expense Tracking').pack(pady=10)
            tk.Label(self.root, textvariable=txt).pack(pady=10)
            tk.Label(self.root, text='Goal amount:').pack(pady=10)
        self.root.mainloop()
        self.root.destroy()  # Destroy the window after mainloop ends
    
    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu
