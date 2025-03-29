import os
import tkinter as tk
from create_account import CAmenu

class Slct:
    def __init__(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(__file__)

        # List all CSV files in the current directory
        csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]

        # Create a new tkinter window to select a CSV file
        self.root = tk.Tk()
        self.root.title('Select CSV File for Pie Chart')

        tk.Label(self.root, text='Select a CSV File:').pack(pady=5)

        # Create a Listbox to display CSV file names
        csv_listbox = tk.Listbox(self.root, height=10, width=50)
        csv_listbox.pack(pady=5)

        # Populate the Listbox with CSV file names
        for csv_file in csv_files:
            csv_listbox.insert(tk.END, csv_file)

        def give_flepth():
            # Get the selected file name
            selected_file_name = csv_listbox.get(csv_listbox.curselection())
            # Construct the full file path
            self.selected_file = os.path.join(current_dir, selected_file_name)
            self.root.quit()  # Exit the mainloop instead of destroying the window

        # Create a button to select the currently selected CSV file
        tk.Button(self.root, text='Select CSV File', command=give_flepth).pack(pady=10)
        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).pack(pady=10)
        tk.Button(self.root, text='Create new account', command=self.restart_main_menu).pack(pady=10)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())
        self.selected_file = None

        self.root.mainloop()
        self.root.destroy()  # Destroy the window after mainloop ends

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main(0)  # Restart the main menu
