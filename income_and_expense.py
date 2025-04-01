import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from slct_prfl import Slct
from datetime import datetime
import csv


class Baimenu:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.expenses = []
        self.income = []
        self.txt = tk.StringVar()
        self.whole = []
        self.starttime = tk.StringVar()
        self.endtime = tk.StringVar()
        self.txt2 = tk.StringVar()
        self.txt3 = tk.StringVar()
        self.is_valid = True

        self.root.title('Income and Expense Tracking')

        # Proceed with using the file path
        try:
            if self.file_path:
                with open(self.file_path, 'r') as file:
                    data = csv.reader(file)
                    for row in data:
                        self.whole.append(row)
                self.income.append(self.whole[2])
                self.expenses.append(self.whole[3])
        except:
            self.is_valid = False

        # Add UI elements
        tk.Label(self.root, text='Income and Expense Tracking').grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text='Add expenses', command=self.add_expenses).grid(row=1, column=0, pady=10, padx=10)
        tk.Button(self.root, text='Add income', command=self.add_income).grid(row=1, column=1, pady=10, padx=10)
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=3, column=0, columnspan=2, pady=20, padx=10)

        if self.is_valid == True:
            tk.Button(self.root, text='Income in timeframe', command=self.time_income).grid(row=2, column=0, pady=10, padx=10)
            tk.Button(self.root, text='Expenses in timeframe', command=self.time_expenses).grid(row=2, column=1, pady=10, padx=10)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def add_expenses(self):
        """Add an expense and save it to the file."""
        self.format = ''  # Reset the format
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create UI for adding an expense
        tk.Label(self.root, text='Amount of expense:').grid(row=0, column=0, pady=10)
        tk.Entry(self.root, textvariable=self.txt).grid(row=0, column=1, pady=10)
        tk.Label(self.root, text='Catagory of expense:').grid(row=1, column=0, pady=10)
        tk.Entry(self.root, textvariable=self.txt2).grid(row=1, column=1, pady=10)
        tk.Button(self.root, text='Enter information', command=self.submit_expense).grid(row=2, column=1, pady=10)
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=2, column=0, pady=20, padx=10)

        # Create the Listbox widget
        tk.Label(self.root, text='Previous sources of expenses:').grid(row=0, column=2, pady=10)
        self.listbox = tk.Listbox(self.root, height=10, width=20)
        self.listbox.grid(row=1, column=2, rowspan=2, pady=10)

        # Populate the Listbox with items
        items = self.whole[1]  # Assuming self.whole[1] contains the list of items
        for item in items:
            try:
                parts = item.split('_')  # Split the item into parts
                if len(parts) > 1:
                    self.listbox.insert(tk.END, parts[1])  # Insert the second part (e.g., "food")
                else:
                    self.listbox.insert(tk.END, item)  # Insert the whole item if no underscore
            except Exception as e:
                pass

    def submit_expense(self):
        """Submit the expense and save it to the file."""
        try:
            # Format the expense with the current date
            self.format = f"{datetime.now().strftime('%Y-%m-%d')}_{self.txt.get()}_{self.txt2.get()}"

            # Validate the input
            if not self.txt.get().strip() or not self.txt.get().isdigit():
                tk.messagebox.showerror("Error", "Please enter a valid expense amount.")
                return

            # Update the total amount in the CSV file
            current_total = float(self.whole[0][0])  # Get the current total from row 1, column 1
            new_total = current_total - float(self.txt.get())  # Subtract the expense from the total
            self.whole[0][0] = str(new_total)  # Update the total in the data structure

            # Append the formatted expense to the expenses list
            self.whole[3].append(self.format)

            # Write the updated data to the CSV file
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in self.whole:
                    writer.writerow(row)

            # Show a success message
            tk.messagebox.showinfo("Success", "Expense added successfully!")

            # Restart the main menu
            self.restart_main_menu()

        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def add_income(self):
        """Add an income and save it to the file."""
        self.format = ''  # Reset the format
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create UI for adding an income
        tk.Label(self.root, text='Amount of income:').grid(row=0, column=0, pady=10)
        tk.Entry(self.root, textvariable=self.txt).grid(row=0, column=1, pady=10)
        tk.Label(self.root, text='Source of income:').grid(row=1, column=0, pady=10)
        tk.Entry(self.root, textvariable=self.txt2).grid(row=1, column=1, pady=10)
        tk.Button(self.root, text='Enter information', command=self.submit_income).grid(row=2, column=1, pady=10)
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=2, column=0, pady=20, padx=10)

    def submit_income(self):
        """Submit the income and save it to the file."""
        try:
            # Format the income with the current date
            self.format = f"{datetime.now().strftime('%Y-%m-%d')}_{self.txt.get()}_{self.txt2.get()}"

            # Validate the input
            if not self.txt.get().strip() or not self.txt.get().isdigit():
                tk.messagebox.showerror("Error", "Please enter a valid income amount.")
                return

            # Update the total amount in the CSV file
            current_total = float(self.whole[0][0])  # Get the current total from row 1, column 1
            new_total = current_total + float(self.txt.get())  # Add the income to the total
            self.whole[0][0] = str(new_total)  # Update the total in the data structure

            # Append the formatted income to the income list
            self.whole[2].append(self.format)

            # Write the updated data to the CSV file
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in self.whole:
                    writer.writerow(row)

            # Show a success message
            tk.messagebox.showinfo("Success", "Income added successfully!")

            # Restart the main menu
            self.restart_main_menu()

        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def show_times_income(self):
        try:
            # Convert start and end times to datetime objects
            start_date_obj = datetime.strptime(self.starttime.get(), "%Y-%m-%d")
            end_date_obj = datetime.strptime(self.endtime.get(), "%Y-%m-%d")

            # Filter income entries within the date range
            filtered_income = []
            for entry in self.income[0]:  # Assuming self.income[0] contains income entries
                date_str, amount = entry.split("_")  # Split the entry into date and amount
                entry_date = datetime.strptime(date_str, "%Y-%m-%d")
                if start_date_obj <= entry_date <= end_date_obj:
                    filtered_income.append(f"{date_str}: {amount}")

            # Clear the current UI
            for widget in self.root.winfo_children():
                widget.destroy()

            # Display the filtered income in a listbox
            tk.Label(self.root, text="Income in the selected timeframe:").grid(row=0, column=0, columnspan=2, pady=10)
            income_listbox = tk.Listbox(self.root, width=50, height=15)
            income_listbox.grid(row=1, column=0, columnspan=2, pady=10)

            for income in filtered_income:
                income_listbox.insert(tk.END, income)

            # Add a back button
            tk.Button(self.root, text="Back", command=self.restart_main_menu).grid(row=2, column=0, columnspan=2, pady=10)

        except ValueError:
            tk.messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

    def show_times_expenses(self):
        try:
            # Convert start and end times to datetime objects
            start_date_obj = datetime.strptime(self.starttime.get(), "%Y-%m-%d")
            end_date_obj = datetime.strptime(self.endtime.get(), "%Y-%m-%d")

            # Filter expense entries within the date range
            filtered_expenses = []
            for entry in self.expenses[0]:  # Assuming self.expenses[0] contains expense entries
                date_str, amount = entry.split("_")  # Split the entry into date and amount
                entry_date = datetime.strptime(date_str, "%Y-%m-%d")
                if start_date_obj <= entry_date <= end_date_obj:
                    filtered_expenses.append(f"{date_str}: {amount}")

            # Clear the current UI
            for widget in self.root.winfo_children():
                widget.destroy()

            # Display the filtered expenses in a listbox
            tk.Label(self.root, text="Expenses in the selected timeframe:").grid(row=0, column=0, columnspan=2, pady=10)
            expenses_listbox = tk.Listbox(self.root, width=50, height=15)
            expenses_listbox.grid(row=1, column=0, columnspan=2, pady=10)

            for expense in filtered_expenses:
                expenses_listbox.insert(tk.END, expense)

            # Add a back button
            tk.Button(self.root, text="Back", command=self.restart_main_menu).grid(row=2, column=0, columnspan=2, pady=10)

        except ValueError:
            tk.messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

    def time_income(self):
        """Create UI for selecting start and end dates for income filtering."""
        self.create_date_selection_ui(self.show_times_income)

    def time_expenses(self):
        """Create UI for selecting start and end dates for expense filtering."""
        self.create_date_selection_ui(self.show_times_expenses)

    def create_date_selection_ui(self, callback):
        """Create a UI for selecting start and end dates."""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Select Start Date:").grid(row=0, column=0, columnspan=3, pady=10)

        # Start date selection
        tk.Label(self.root, text="Year:").grid(row=1, column=0, padx=5, pady=5)
        start_year_combo = ttk.Combobox(self.root, values=[str(i) for i in range(2000, datetime.now().year + 1)], state="readonly", width=5)
        start_year_combo.grid(row=1, column=1, padx=5, pady=5)
        start_year_combo.set(datetime.now().strftime("%Y"))

        tk.Label(self.root, text="Month:").grid(row=2, column=0, padx=5, pady=5)
        start_month_combo = ttk.Combobox(self.root, values=[f"{i:02d}" for i in range(1, 13)], state="readonly", width=5)
        start_month_combo.grid(row=2, column=1, padx=5, pady=5)
        start_month_combo.set(datetime.now().strftime("%m"))

        tk.Label(self.root, text="Day:").grid(row=3, column=0, padx=5, pady=5)
        start_day_combo = ttk.Combobox(self.root, values=[f"{i:02d}" for i in range(1, 32)], state="readonly", width=5)
        start_day_combo.grid(row=3, column=1, padx=5, pady=5)
        start_day_combo.set(datetime.now().strftime("%d"))

        tk.Label(self.root, text="Select End Date:").grid(row=4, column=0, columnspan=3, pady=10)

        # End date selection
        tk.Label(self.root, text="Year:").grid(row=5, column=0, padx=5, pady=5)
        end_year_combo = ttk.Combobox(self.root, values=[str(i) for i in range(2000, datetime.now().year + 1)], state="readonly", width=5)
        end_year_combo.grid(row=5, column=1, padx=5, pady=5)
        end_year_combo.set(datetime.now().strftime("%Y"))

        tk.Label(self.root, text="Month:").grid(row=6, column=0, padx=5, pady=5)
        end_month_combo = ttk.Combobox(self.root, values=[f"{i:02d}" for i in range(1, 13)], state="readonly", width=5)
        end_month_combo.grid(row=6, column=1, padx=5, pady=5)
        end_month_combo.set(datetime.now().strftime("%m"))

        tk.Label(self.root, text="Day:").grid(row=7, column=0, padx=5, pady=5)
        end_day_combo = ttk.Combobox(self.root, values=[f"{i:02d}" for i in range(1, 32)], state="readonly", width=5)
        end_day_combo.grid(row=7, column=1, padx=5, pady=5)
        end_day_combo.set(datetime.now().strftime("%d"))

        # Submit button
        tk.Button(
            self.root,
            text="Submit",
            command=lambda: self.get_selected_dates(
                start_day_combo, start_month_combo, start_year_combo,
                end_day_combo, end_month_combo, end_year_combo,
                callback
            )
        ).grid(row=8, column=0, columnspan=3, pady=10)

    def get_selected_dates(self, start_day_combo, start_month_combo, start_year_combo,
                           end_day_combo, end_month_combo, end_year_combo, callback):
        """Retrieve the selected start and end dates and store them."""
        start_day = start_day_combo.get()
        start_month = start_month_combo.get()
        start_year = start_year_combo.get()
        end_day = end_day_combo.get()
        end_month = end_month_combo.get()
        end_year = end_year_combo.get()

        try:
            # Validate the selected start and end dates
            start_date = datetime.strptime(f"{start_year}-{start_month}-{start_day}", "%Y-%m-%d")
            end_date = datetime.strptime(f"{end_year}-{end_month}-{end_day}", "%Y-%m-%d")

            if start_date > end_date:
                raise ValueError("Start date cannot be after end date.")

            self.starttime.set(start_date.strftime("%Y-%m-%d"))
            self.endtime.set(end_date.strftime("%Y-%m-%d"))

            # Call the callback function (e.g., show_times_income or show_times_expenses)
            callback()

        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def restart_main_menu(self):
        if self.root.winfo_exists():
            self.root.destroy()
        from main import main
        main()
