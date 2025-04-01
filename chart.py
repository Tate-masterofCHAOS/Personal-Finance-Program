import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv
from slct_prfl import Slct  # Import the Slct class from slct_prfl.py


class Charts:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path

        # Initialize an empty list to store all rows
        self.data_rows = []

        # Proceed with using the file path
        if self.file_path:
            try:
                with open(self.file_path, 'r') as file:
                    reader = csv.reader(file)
                    # Read all rows and store them in self.data_rows
                    self.data_rows = [row for row in reader]
                self.generate_pie_chart()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read the file: {e}")
                self.restart_main_menu()
        else:
            messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            self.restart_main_menu()

    def generate_pie_chart(self):
        """Generate a pie chart based on the expense data and total amount."""
        for widget in self.root.winfo_children():
            widget.destroy()  # Clear the current UI

        # Ensure there are enough rows in the data
        if len(self.data_rows) > 1:
            try:
                # Get the total amount from line 1, column 1
                total_amount = float(self.data_rows[0][0])

                # Assuming the second row contains expense data
                expenses = self.data_rows[1]  # Example: ['100_food', '200_rent', ...]

                labels = []
                sizes = []

                # Process each item in the expenses row
                for item in expenses:
                    try:
                        size, label = item.split('_')  # Split the string (e.g., '100_food') into size and label
                        labels.append(label.strip())  # Add the label to the labels list
                        sizes.append(float(size))  # Add the size (converted to float) to the sizes list
                    except ValueError:
                        messagebox.showerror("Error", f"Invalid data format in expenses: {item}")
                        self.restart_main_menu()
                        return

                # Calculate the total of all expenses
                total_expenses = sum(sizes)

                # Check if the total is valid
                if total_expenses > total_amount:
                    messagebox.showerror("Error", "Total expenses exceed the total amount.")
                    self.restart_main_menu()
                    return

                # Add the "Remaining" amount to the pie chart if there is any leftover
                remaining_amount = total_amount - total_expenses
                if remaining_amount > 0:
                    labels.append("Remaining")
                    sizes.append(remaining_amount)
                self.restart_main_menu()
                # Generate the pie chart
                plt.figure(figsize=(8, 8))  # Set the figure size
                plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
                plt.title('Pie Chart of Expenses')
                plt.show()

            except ValueError:
                messagebox.showerror("Error", "Invalid data format in the total amount.")
                self.restart_main_menu()
        else:
            messagebox.showerror("Error", "Not enough data to generate a pie chart.")

    def restart_main_menu(self):
        """Display a menu with options to return to the main menu or generate another chart."""
        for widget in self.root.winfo_children():
            widget.destroy()  # Clear the current UI

        # Add a label
        tk.Label(self.root, text="What would you like to do next?").grid(row=0, column=0, columnspan=2, pady=20)

        # Add buttons for options
        tk.Button(self.root, text="Generate Another Chart", command=self.generate_pie_chart, width=20).grid(row=1, column=0, pady=10, padx=10)
        tk.Button(self.root, text="Return to Main Menu", command=self.exit_to_main_menu, width=20).grid(row=1, column=1, pady=10, padx=10)

    def exit_to_main_menu(self):
        """Exit to the main menu."""
        self.root.destroy()  # Close the current window
        from main import main  # Import the main menu function
        main()  # Restart the main menu
