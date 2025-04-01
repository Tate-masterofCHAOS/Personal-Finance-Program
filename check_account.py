import os
import tkinter as tk
import csv

class Chk:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.total = tk.StringVar()
        self.whole = []

        self.root.title('Check Account')

        # Proceed with using the file path
        if self.file_path:
            with open(self.file_path, 'r') as file:
                data = csv.reader(file)
                for row in data:
                    self.whole.append(row)
            self.total.set(f'{self.whole[0][0]}  -  {self.whole[0][1]}')

        tk.Label(self.root, text='Total amount:').grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        tk.Label(self.root, textvariable=self.total, font=("Helvetica", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        # Create a button to go back to the main menu
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=3, column=0, columnspan=2, pady=20, padx=10)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main()  # Restart the main menu
