import os
import tkinter as tk
from tkinter import ttk  # Import themed Tkinter widgets
from datetime import datetime
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
        self.repeat = tk.StringVar()
        self.label = tk.StringVar()
        self.number = tk.StringVar()
        self.total = []

        # Create lists to store the dynamically created entry widgets
        self.expense_labels = []
        self.expense_amounts = []

        # Create UI elements
        self.create_ui()
        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)
        self.root.mainloop()
        self.root.destroy()  # Destroy the window after mainloop ends

    def validate_float(self, value_if_allowed):
        """Validate that the input is a valid float or empty."""
        if value_if_allowed == "":
            return True  # Allow empty input
        try:
            float(value_if_allowed)
            return True  # Input is a valid float
        except ValueError:
            return False  # Input is not a valid float

    def create_ui(self):
        # Register the validation command
        self.validate_cmd = (self.root.register(self.validate_float), "%P")

        # Use grid layout manager for all widgets
        tk.Label(self.root, text='Please enter the following information:').grid(row=0, column=0, columnspan=2, pady=5)

        # Account Name
        tk.Label(self.root, text='Account Name:').grid(row=1, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.acnt_name).grid(row=1, column=1, pady=5, sticky='w')

        # Total Amount
        tk.Label(self.root, text='Total amount:').grid(row=2, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.total_amnt, validate="key", validatecommand=self.validate_cmd).grid(row=2, column=1, pady=5, sticky='w')

        # Type of Currency
        tk.Label(self.root, text='Type of currency:').grid(row=3, column=0, pady=5, sticky='e')
        ttk.Combobox(self.root, textvariable=self.type, values=["USD", "EUR", "GBP", "JPY"], state='readonly').grid(row=3, column=1, pady=5, sticky='w')

        # Goal Amount
        tk.Label(self.root, text='Goal amount:').grid(row=4, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.goal_amnt, validate="key", validatecommand=self.validate_cmd).grid(row=4, column=1, pady=5, sticky='w')

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
                round(total_amnt_float, 2),
                self.type.get(),
                round(goal_amnt_float, 2),
                self.date_access,
            ]

            # Clear all widgets in the root window
            for widget in self.root.winfo_children():
                widget.destroy()

            # Create a new frame for the "Goals" section
            tk.Label(self.root, text='How many types of expenses are there?').grid(row=1, column=0, pady=5)
            tk.Entry(self.root, textvariable=self.repeat, validate="key", validatecommand=self.validate_cmd).grid(row=1, column=1, pady=5, sticky='w')

            # Add a button to confirm the input
            tk.Button(self.root, text="Confirm", command=self.validate_repeat_input).grid(row=2, column=1, pady=10)

        except FileNotFoundError:
            # Show an error message if the file is not found
            tk.messagebox.showerror("Error", "File not found. Please check the file path.")
        except ValueError:
            # Show an error message if conversion fails
            tk.messagebox.showerror("Invalid Input", "Total amount and Goal amount must be valid numbers.")

    def validate_repeat_input(self):
        """Validate the 'repeat' input and proceed if valid."""
        repeat_value = self.repeat.get().strip()
        if not repeat_value.isdigit() or int(repeat_value) <= 0:
            tk.messagebox.showerror("Invalid Input", "Please enter a valid positive integer for the number of expenses.")
            return  # Do not proceed if the input is invalid

        # Clear all widgets in the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Dynamically create entry fields for the number of expenses
        self.create_expense_entries(int(repeat_value))

    def create_expense_entries(self, num_expenses):
        """Dynamically create entry fields for expense labels and amounts."""
        for i in range(num_expenses):
            # Label for the expense type
            tk.Label(self.root, text=f'Enter type of expense {i + 1}:').grid(row=i + 2, column=0, pady=5, sticky='e')
            label_entry = tk.Entry(self.root)  # Entry for the expense label
            label_entry.grid(row=i + 2, column=1, pady=5, sticky='w')
            self.expense_labels.append(label_entry)  # Store the label entry widget

            # Label for the expense amount
            tk.Label(self.root, text=f'Enter amount for expense {i + 1}:').grid(row=i + 2, column=2, pady=5, sticky='e')
            amount_entry = tk.Entry(self.root, validate="key", validatecommand=self.validate_cmd)  # Entry for the expense amount
            amount_entry.grid(row=i + 2, column=3, pady=5, sticky='w')
            self.expense_amounts.append(amount_entry)  # Store the amount entry widget

        # Add a button to confirm and save the expenses
        tk.Button(self.root, text="Save Expenses", command=self.save_expenses).grid(row=num_expenses + 2, column=1, pady=10)

    def save_expenses(self):
        """Collect and save the expense data."""
        expenses = []
        for label_entry, amount_entry in zip(self.expense_labels, self.expense_amounts):
            label = label_entry.get().strip()  # Get the label text
            amount = amount_entry.get().strip()  # Get the amount text
            if label and amount:  # Ensure both fields are filled
                try:
                    formatted_expense = f"{int(amount)}_{label}"  # Format as "amount_label"
                    expenses.append(formatted_expense)  # Add to the expenses list
                except ValueError:
                    tk.messagebox.showerror("Invalid Input", f"Invalid amount for expense '{label}'. Please enter a valid number.")
                    return

        # Write the data and expenses to the CSV file
        file_name = f"{self.acnt_name.get()}_account.csv"
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.total_amnt.get(), self.type.get(), self.goal_amnt.get(), self.date_access])  # Write the main account data
            writer.writerow(expenses)  # Write the expenses as a separate row
            writer.writerow('0000-00-00_0_***')
            writer.writerow('0000-00-00_0_***')

        # Show a success message
        tk.messagebox.showinfo("Success", f"Account information and expenses saved to {file_name}!")

        # Restart the main menu
        self.restart_main_menu()

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main()  # Restart the main menu