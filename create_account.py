import os
import tkinter as tk
from tkinter import ttk  # Import themed Tkinter widgets
from datetime import datetime
import pandas as pd
import csv
from tkinter import messagebox

class CAmenu:
    def __init__(self, root):
        # Create a new tkinter window to select a CSV file
        self.root = root
        self.root.title('Create Account')
        self.acnt_name = tk.StringVar()
        self.total_amnt = tk.StringVar()
        self.type = tk.StringVar()
        self.goal_amnt = tk.StringVar()
        self.date_access = datetime.now().strftime('%Y-%m-%d')
        self.data_frame = None
        self.callback = None

        # Create UI elements
        self.create_ui()
        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def validate_float(self, value_if_allowed):
        if value_if_allowed == "":
            return True  # Allow empty input
        try:
            float(value_if_allowed)
            return True  # Input is a valid float
        except ValueError:
            return False  # Input is not a valid float

    def create_ui(self):
        # Use grid layout manager for all widgets
        tk.Label(self.root, text='Please enter the following information:').grid(row=0, column=0, columnspan=2, pady=5)

        # Account Name
        tk.Label(self.root, text='Account Name:').grid(row=1, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.acnt_name).grid(row=1, column=1, pady=5, sticky='w')

        # Validation command for float-only input
        validate_cmd = (self.root.register(self.validate_float), "%P")

        # Total Amount
        tk.Label(self.root, text='Total amount:').grid(row=2, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.total_amnt, validate="key", validatecommand=validate_cmd).grid(row=2, column=1, pady=5, sticky='w')

        # Type of Currency
        tk.Label(self.root, text='Type of currency:').grid(row=3, column=0, pady=5, sticky='e')
        ttk.Combobox(self.root, textvariable=self.type, values=["USD", "EUR", "GBP", "JPY"], state='readonly').grid(row=3, column=1, pady=5, sticky='w')

        # Goal Amount
        tk.Label(self.root, text='Goal amount:').grid(row=4, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.goal_amnt, validate="key", validatecommand=validate_cmd).grid(row=4, column=1, pady=5, sticky='w')

        # Enter Information Button
        tk.Button(self.root, text='Enter information', command=self.submit_information).grid(row=5, column=1, pady=10)
        # Back to Menu Button
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=5, column=0, pady=10)

    def submit_information(self):
        """Validate and save the entered information to a CSV file."""
        try:
            current_dir = os.path.dirname(__file__)

            # List all CSV files in the current directory
            csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
            if f'{self.acnt_name.get()}_account.csv' in csv_files:
                tk.messagebox.showerror("Error", "Account name already exists. Please choose a different name.")
                return CAmenu(self.root)

            # Convert total amount and goal amount to floats
            total_amnt_float = float(self.total_amnt.get())
            goal_amnt_float = float(self.goal_amnt.get())

            # Collect the data as a list of values (no labels)
            data = [
                total_amnt_float.round(2),
                self.type.get(),
                goal_amnt_float.round(2),
                self.date_access,
            ]

            # Save the data to a new CSV file without labels
            file_name = f"{self.acnt_name.get()}_account.csv"
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)  # Write the data as a single row

            # Show a success message
            tk.messagebox.showinfo("Success", f"Account information saved to {file_name}!")

            # Call the callback function if it exists
            if self.callback:
                self.callback(data)
            self.restart_main_menu()  # Restart the main menu after saving

        except FileNotFoundError:   
            # Show an error message if the file is not found
            tk.messagebox.showerror("Error", "File not found. Please check the file path.")
        except ValueError:
            # Show an error message if conversion fails
            tk.messagebox.showerror("Invalid Input", "Total amount and Goal amount must be valid numbers.")

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu