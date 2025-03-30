import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv


class Budge_shw:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.data_rows = []

        self.root.title('Budget Categories')

        # Load data from the file
        if self.file_path:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                self.data_rows = [row for row in reader]

        # Add UI elements
        tk.Label(self.root, text='Budget Categories:').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text='Expense Max:').grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.root, text='Type of Expense:').grid(row=1, column=1, padx=10, pady=10)

        # Create Listbox widgets
        self.listbox_1 = tk.Listbox(self.root, height=10, width=20)
        self.listbox_1.grid(row=2, column=0, padx=10, pady=10)
        self.listbox_2 = tk.Listbox(self.root, height=10, width=20)
        self.listbox_2.grid(row=2, column=1, padx=10, pady=10)

        # Populate the Listboxes
        if len(self.data_rows) > 1:
            for item in self.data_rows[1]:
                parts = item.split('_')
                if len(parts) == 2:
                    self.listbox_1.insert(tk.END, parts[0])  # Expense max
                    self.listbox_2.insert(tk.END, parts[1])  # Type of expense

        # Add a back button
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=3, column=0, columnspan=2, pady=20)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()
        from main import main
        main()


class Budge:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.txt = tk.StringVar()
        self.txt2 = tk.StringVar()
        self.type = tk.StringVar()
        self.data_rows = []
        self.lst = []

        # Load data from the file
        if self.file_path:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                self.data_rows = [row for row in reader]

        # Populate the dropdown list
        if len(self.data_rows) > 1:
            for item in self.data_rows[1]:
                parts = item.replace('_', '  ')
                self.lst.append(parts)

        # Add UI elements
        self.create_main_menu()

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def create_main_menu(self):
        """Create the main menu for budget management."""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text='Budget Management').grid(row=0, column=0, columnspan=3, pady=10)

        tk.Button(self.root, text='Add Budget Category', command=self.add).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text='Remove Budget Category', command=self.remove).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text='Edit Budget Category', command=self.edit).grid(row=1, column=2, padx=10, pady=10)

        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=2, column=0, columnspan=3, pady=20)

    def add(self):
        """Add a new budget category."""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text='Budget Label:').grid(row=0, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.txt).grid(row=0, column=1, pady=5, sticky='w')
        tk.Label(self.root, text='Budget Amount:').grid(row=1, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.txt2).grid(row=1, column=1, pady=5, sticky='w')

        tk.Button(self.root, text='Save', command=self.add_item).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text='Back to Menu', command=self.create_main_menu).grid(row=3, column=0, columnspan=2, pady=10)

    def add_item(self):
        """Save the new budget category to the file."""
        try:
            amount = self.txt2.get().strip()
            label = self.txt.get().strip()

            if not amount or not label:
                raise ValueError("Both fields must be filled.")
            if not amount.isdigit():
                raise ValueError("Amount must be a valid number.")

            new_item = f"{amount}_{label}"
            if new_item in self.data_rows[1]:
                raise ValueError("This budget category already exists.")

            self.data_rows[1].append(new_item)

            # Write the updated data back to the file
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.data_rows)

            tk.messagebox.showinfo("Success", "Budget category added successfully!")
            self.create_main_menu()

        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def remove(self):
        """Remove an existing budget category."""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text='Select Budget to Remove:').grid(row=0, column=0, pady=5, sticky='e')
        ttk.Combobox(self.root, textvariable=self.type, values=self.lst, state='readonly').grid(row=0, column=1, pady=5, sticky='w')

        tk.Button(self.root, text='Remove', command=self.remove_item).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text='Back to Menu', command=self.create_main_menu).grid(row=2, column=0, columnspan=2, pady=10)

    def remove_item(self):
        """Remove the selected budget category from the file."""
        try:
            selected = self.type.get()
            if not selected:
                raise ValueError("Please select a budget to remove.")

            for item in self.data_rows[1]:
                if item.split('_')[1] == selected.split('  ')[1]:
                    self.data_rows[1].remove(item)
                    break

            # Write the updated data back to the file
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.data_rows)

            tk.messagebox.showinfo("Success", "Budget category removed successfully!")
            self.create_main_menu()

        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def edit(self):
        """Edit an existing budget category."""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text='Select Budget to Edit:').grid(row=0, column=0, pady=5, sticky='e')
        ttk.Combobox(self.root, textvariable=self.type, values=self.lst, state='readonly').grid(row=0, column=1, pady=5, sticky='w')

        tk.Button(self.root, text='Edit', command=self.edit2).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text='Back to Menu', command=self.create_main_menu).grid(row=2, column=0, columnspan=2, pady=10)

    def edit2(self):
        """Edit the selected budget category."""
        selected = self.type.get()
        if not selected:
            messagebox.showerror("Error", "Please select a budget to edit.")
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        split = selected.split('  ')
        self.txt.set(split[1])
        self.txt2.set(split[0])

        tk.Label(self.root, text=f'Edit Budget for {split[1]}:').grid(row=0, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.txt2).grid(row=0, column=1, pady=5, sticky='w')

        tk.Button(self.root, text='Save', command=self.save_edit).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text='Back to Menu', command=self.create_main_menu).grid(row=2, column=0, columnspan=2, pady=10)

    def save_edit(self):
        """Save the edited budget category."""
        try:
            amount = self.txt2.get().strip()
            label = self.txt.get().strip()

            if not amount or not label:
                raise ValueError("Both fields must be filled.")
            if not amount.isdigit():
                raise ValueError("Amount must be a valid number.")

            new_item = f"{amount}_{label}"
            old_item = self.type.get().replace('  ', '_')

            for i, item in enumerate(self.data_rows[1]):
                if item == old_item:
                    self.data_rows[1][i] = new_item
                    break

            # Write the updated data back to the file
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.data_rows)

            tk.messagebox.showinfo("Success", "Budget category updated successfully!")
            self.create_main_menu()

        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()
        from main import main
        main()
