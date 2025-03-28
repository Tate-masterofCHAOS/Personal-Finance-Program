import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


class Charts:
    def __init__(self, root):
        self.root = root
        self.root.title('Charts')
        self.csv_files = []  # To store the list of CSV files
        self.create_ui()

    def create_ui(self):
        # Find all CSV files in the current directory
        self.csv_files = [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.csv')]

        # Create a Listbox to display CSV file names
        self.csv_listbox = tk.Listbox(self.root, height=10, width=50)
        self.csv_listbox.pack(pady=5)

        # Populate the Listbox with CSV file names
        for csv_file in self.csv_files:
            self.csv_listbox.insert(tk.END, csv_file)

        # Create a button to select the currently selected CSV file
        tk.Button(self.root, text='Select CSV File', command=self.generate_pie_chart).pack(pady=10)

        # Create a button to go back to the main menu
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=10)

    def generate_pie_chart(self):
        # Get the selected file index from the Listbox
        selected_file_index = self.csv_listbox.curselection()
        if not selected_file_index:
            messagebox.showerror('Error', 'Please select a CSV file!')
            return

        # Get the selected file name
        selected_file_name = self.csv_listbox.get(selected_file_index[0])

        # Construct the full file path
        file_path = os.path.join(os.path.dirname(__file__), selected_file_name)

        input()

        with open(file_path, 'r') as file:
            lines = file.readlines()
            income = lines[2].strip().split(',')  # Access the desired line
            expense = lines[3].strip().split(',')

        print(income)
        print(expense)

        income_r = []
        expense_r = []

        for item in income:
            item = item.split('_')
            income_r.append(item)

        for item in expense:
            item = item.split('_')
            expense_r.append(item)
        print(income_r)
        print(expense_r)

        print('HECK YESSSSSSSSSS')

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu


if __name__ == "__main__":
    root = tk.Tk()
    app = Charts(root)
    root.mainloop()
