import os
import tkinter as tk
from tkinter import messagebox


class Slct:
    def __init__(self, root, return_to_menu_callback):
        self.root = root
        self.selected_file = None  # Initialize the selected file path
        self.return_to_menu_callback = return_to_menu_callback  # Callback to return to the main menu

        # Add UI elements for file selection
        tk.Label(self.root, text="Select a profile from the list:").pack(pady=10)

        # Create a listbox to display available files
        self.file_listbox = tk.Listbox(self.root, width=50, height=15)
        self.file_listbox.pack(pady=10)

        # Populate the listbox with CSV files from the current directory
        self.populate_file_list()

        # Add buttons for selecting a file and returning to the menu
        tk.Button(self.root, text="Select File", command=self.choose_file).pack(pady=5)
        tk.Button(self.root, text="Return to Menu", command=self.return_to_menu).pack(pady=5)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)

    def populate_file_list(self):
        """Populate the listbox with CSV files from the current directory."""
        current_dir = os.getcwd()  # Get the current working directory
        csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]  # Filter for CSV files

        if not csv_files:
            self.file_listbox.insert(tk.END, "No CSV files found.")  # Show a message if no files are found
            self.file_listbox.config(state=tk.DISABLED)  # Disable the listbox if no files are available
        else:
            for file in csv_files:
                self.file_listbox.insert(tk.END, file)  # Add each file to the listbox

    def choose_file(self):
        """Set the selected file from the listbox."""
        try:
            selected_index = self.file_listbox.curselection()  # Get the selected index
            if not selected_index:
                raise ValueError("No file selected.")  # Raise an error if no file is selected

            selected_file = self.file_listbox.get(selected_index)  # Get the selected file name
            self.selected_file = os.path.abspath(selected_file)  # Get the absolute path of the selected file
            self.root.destroy()  # Close the window after selecting a file
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Show an error message if no file is selected

    def return_to_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current window
        self.return_to_menu_callback()  # Call the callback to return to the main menu

    def close_window(self):
        """Handle the window close event."""
        self.root.destroy()

    def get_selected_file(self):
        """Return the selected file path."""
        return self.selected_file
