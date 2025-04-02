import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from slct_prfl import Slct
import csv
import pandas as pd

class Cc:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.txt = tk.StringVar()
        self.data_rows = []
        self.type = tk.StringVar()
        self.lst = ["USD", "EUR", "GBP", "JPY"]

        # Proceed with using the file path
        if self.file_path:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                self.data_rows = [row for row in reader]
        self.lst.remove(self.data_rows[0][1])

        # Add UI elements
        tk.Label(self.root, text='Change Currency').grid(row=0, column=0, columnspan=2, pady=5)
        tk.Label(self.root, text='Enter new currency:').grid(row=1, column=0, pady=5, sticky='e')
        ttk.Combobox(self.root, textvariable=self.type, values=self.lst, state='readonly').grid(row=1, column=1, pady=5, sticky='w')
        tk.Label(self.root, text='Note! This is not exact, numbers may get bigger or smaller.').grid(row=2, column=0, columnspan=2, pady=5, sticky='e')
        tk.Button(self.root, text='Save', command=self.save_currency).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=4, column=0, columnspan=2, pady=5)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)
        self.root.mainloop()

    def save_currency(self):
        """Save the new currency to the CSV file."""
        new_currency = self.type.get()
        if not new_currency:
            messagebox.showerror("Error", "Please select a currency.")
            return
        if new_currency == self.data_rows[0][1]:
            messagebox.showinfo("Info", "Currency is already set to this value.")
            return

        # Conversion logic
        try:
            if new_currency == 'GBP':
                if self.data_rows[0][1] == 'USD':
                    conversion_rate = 0.77  # USD to GBP
                elif self.data_rows[0][1] == 'EUR':
                    conversion_rate = 0.86  # EUR to GBP
                elif self.data_rows[0][1] == 'JPY':
                    conversion_rate = 0.0051  # JPY to GBP
                else:
                    raise ValueError("Unsupported currency conversion.")
            elif new_currency == 'EUR':
                if self.data_rows[0][1] == 'USD':
                    conversion_rate = 0.88  # USD to EUR
                elif self.data_rows[0][1] == 'GBP':
                    conversion_rate = 1.16  # GBP to EUR
                elif self.data_rows[0][1] == 'JPY':
                    conversion_rate = 0.0060  # JPY to EUR
                else:
                    raise ValueError("Unsupported currency conversion.")
            elif new_currency == 'USD':
                if self.data_rows[0][1] == 'GBP':
                    conversion_rate = 1.30  # GBP to USD
                elif self.data_rows[0][1] == 'EUR':
                    conversion_rate = 1.14  # EUR to USD
                elif self.data_rows[0][1] == 'JPY':
                    conversion_rate = 0.0091  # JPY to USD
                else:
                    raise ValueError("Unsupported currency conversion.")
            elif new_currency == 'JPY':
                if self.data_rows[0][1] == 'USD':
                    conversion_rate = 110.0  # USD to JPY
                elif self.data_rows[0][1] == 'GBP':
                    conversion_rate = 150.0  # GBP to JPY
                elif self.data_rows[0][1] == 'EUR':
                    conversion_rate = 130.0  # EUR to JPY
                else:
                    raise ValueError("Unsupported currency conversion.")
            else:
                raise ValueError("Unsupported currency selected.")

            # Apply the conversion rate to all relevant rows
            self.data_rows[0][0] = round(float(self.data_rows[0][0]) * conversion_rate, 2)  # Update total amount
            self.data_rows[0][1] = new_currency  # Update currency type
            try:
                for i in range(len(self.data_rows[1])):  # Update row 2 (expenses)
                    money, label = self.data_rows[1][i].split('_')
                    money = round(float(money) * conversion_rate, 2)
                    self.data_rows[1][i] = f"{money}_{label}"
            except:
                messagebox.showinfo("Info", "Budgets is not written")

            try:
                for i in range(len(self.data_rows[2])):  # Update row 3 (income)
                    date, money = self.data_rows[2][i].split('_')
                    money = round(float(money) * conversion_rate, 2)
                    self.data_rows[2][i] = f"{date}_{money}"
            except:
                messagebox.showinfo("Info", "Income is not written")

            try:
                for i in range(len(self.data_rows[3])):  # Update row 4 (expenses with dates)
                    date, money = self.data_rows[3][i].split('_')
                    money = round(float(money) * conversion_rate, 2)
                    self.data_rows[3][i] = f"{date}_{money}"
            except:
                messagebox.showinfo("Info", "Expenses are not written")

            # Write the updated data back to the CSV file
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.data_rows)

            messagebox.showinfo("Success", f"Currency changed to {new_currency}.")
            self.restart_main_menu()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main()  # Restart the main menu