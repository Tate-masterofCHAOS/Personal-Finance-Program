import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv
from slct_prfl import Slct  # Import the Slct class from slct_prfl.py


class Charts:
    def __init__(self, root):
        file_path = Slct().selected_file
        print(f"Selected file path: {file_path}")

        # Initialize an empty list to store all rows
        self.data_rows = []

        # Proceed with using the file path
        if file_path:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                # Read all rows and store them in self.data_rows
                self.data_rows = [row for row in reader]
            self.generate_pie_chart()

        self.root.mainloop()
        self.root.destroy()  # Destroy the window after mainloop ends

    def generate_pie_chart(self):
        # Ensure there are enough rows in the data
        if len(self.data_rows) > 1:
            # Assuming the second row contains expense data
            expenses = self.data_rows[1]  # Example: ['100_food', '200_rent', ...]

            labels = []
            sizes = []

            # Process each item in the expenses row
            for item in expenses:
                # Split the string (e.g., '100_food') into size and label
                size, label = item.split('_')
                labels.append(label)  # Add the label to the labels list
                sizes.append(int(size))  # Add the size (converted to int) to the sizes list

            # Check if the total is valid
            total = sum(sizes)
            if total <= 0:
                messagebox.showerror("Error", "Total amount is less than or equal to zero.")
                return

            # Generate the pie chart
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title('Pie Chart of Expenses')
            plt.show()
    

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Destroy the current window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu
