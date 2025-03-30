import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from slct_prfl import Slct
import csv
import pandas as pd

class Gmenu:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.txt = tk.StringVar()
        self.data_rows = []

        self.root.title('Goals')

        # Proceed with using the file path
        if self.file_path:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                self.data_rows = [row for row in reader]

        # Add UI elements
        tk.Label(self.root, text='Goals').pack(pady=10)
        tk.Label(self.root, text='Goal amount:').pack(pady=3)
        tk.Label(self.root, textvariable=self.txt, font=("Helvetica", 12, "bold")).pack(pady=3)
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=20)

        # Display the goal amount
        self.display()

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def display(self):
        """Display the goal amount from the data."""
        if self.data_rows:
            self.txt.set(self.data_rows[0][2])  # Set the text variable to the goal amount

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main()  # Restart the main menu

class Gset:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.txt = tk.StringVar()

        # Initialize an empty list to store all rows
        self.data_rows = []

        # Proceed with using the file path
        if self.file_path:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                # Read all rows and store them in self.data_rows
                self.data_rows = [row for row in reader]

        # Add UI elements
        self.root.title('Edit Goal')
        tk.Label(self.root, text='Edit Goal Amount').pack(pady=10)
        tk.Entry(self.root, textvariable=self.txt).pack(pady=10)
        tk.Button(self.root, text='Save Goal', command=self.save_goal).pack(pady=10)
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=10)

        # Display the current goal amount
        self.display()

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def display(self):
        """Display the current goal amount."""
        if self.data_rows:
            self.txt.set(self.data_rows[0][2])  # Set the text variable to the current goal amount

    def save_goal(self):
        """Save the updated goal amount to the file."""
        try:
            new_goal = self.txt.get().strip()
            if not new_goal.isdigit():
                raise ValueError("Goal amount must be a valid number.")

            # Update the goal amount in the data structure
            self.data_rows[0][2] = new_goal

            # Write the updated data back to the file
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.data_rows)

            tk.messagebox.showinfo("Success", "Goal amount updated successfully!")
            self.restart_main_menu()

        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current window
        from main import main  # Import the main menu function
        main()
