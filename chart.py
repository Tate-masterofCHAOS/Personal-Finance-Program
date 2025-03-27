import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class Charts:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Charts')

        self.text_display = tk.Text(self.root, height=20, width=50, state=tk.DISABLED)
        self.text_display.pack()

        self.game_button = tk.Button(self.root, text='Start Game', command=self.start_game)
        self.game_button.pack()

        self.menu_button = tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu)
        self.menu_button.pack()

        self.continue_button = None
        self.valid_prfl = None
        self.enmy_prfl = None
        self.base_prfl = None
        self.enmy_base_prfl = None
        self.win = 1
        self.turn = 1

    def update_display(self, text):
        self.text_display.config(state=tk.NORMAL)
        self.text_display.insert(tk.END, text + '\n')
        self.text_display.config(state=tk.DISABLED)



def matplotlib_display_pie_chart():
    """Display a pie chart of a character's stats using Matplotlib."""
    csv_files = [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.csv')]

    # Create a new tkinter window to select a CSV file

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    selection_window = tk.Toplevel()
    selection_window.title('Select CSV File for Pie Chart')

    tk.Label(selection_window, text='Select a CSV File:').pack(pady=5)

    # Create a Listbox to display CSV file names
    csv_listbox = tk.Listbox(selection_window, height=10, width=50)
    csv_listbox.pack(pady=5)

    # THIS MAKES THE ITEMS IN THE LIST TO SELECT
    for csv_file in csv_files:
        csv_listbox.insert(tk.END, csv_file)

    def generate_pie_chart():
        # Get the selected CSV file
        selected_index = csv_listbox.curselection()
        if not selected_index:
            messagebox.showerror('Error', 'Please select a CSV file!')
            return

        selected_csv = csv_files[selected_index[0]]

        # Load the selected CSV file into a DataFrame
        csv_path = os.path.join(os.path.dirname(__file__), selected_csv)
        df = pd.read_csv(csv_path)

        # Create a new tkinter window to select a character
        character_selection_window = tk.Toplevel()
        character_selection_window.title('Select Character for Pie Chart')

        tk.Label(character_selection_window, text='Select a Character:').pack(pady=5)

        # Create a Listbox to display character names
        character_listbox = tk.Listbox(character_selection_window, height=10, width=50)
        character_listbox.pack(pady=5)

        # Populate the Listbox with character names
        for name in df['NAME']:
            character_listbox.insert(tk.END, name)

        def generate_character_pie_chart():
            # Get the selected character
            selected_character_index = character_listbox.curselection()
            if not selected_character_index:
                messagebox.showerror('Error', 'Please select a character!')
                return

            character_name = df['NAME'].iloc[selected_character_index[0]]

            # Filter the DataFrame for the selected character
            character_data = df[df['NAME'] == character_name]

            # Extract stats for the character
            stats = ['DAMAGE', 'ARMOUR', 'DODGE', 'HEALTH', 'REGEN']
            values = character_data[stats].iloc[0].tolist()

            # Create a pie chart
            plt.figure(figsize=(6, 6))
            plt.pie(values, labels=stats, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(np.linspace(0, 1, len(stats))))
            plt.title(f"{character_name}'s Stats")
            plt.show()

            # Close the character selection window after generating the chart
            character_selection_window.destroy()

        tk.Button(character_selection_window, text='Generate Pie Chart', command=generate_character_pie_chart).pack(pady=10)

        # Close the CSV selection window
        selection_window.destroy()

    # THIS ONE CREATES A BUTTON THAT RUNS THE FUNCTION, SELECTING THE CURRENTLY SELECTED CSV FILE
    tk.Button(selection_window, text='Select CSV File', command=generate_pie_chart).pack(pady=10)

    # Keep the tkinter main loop running
    selection_window.protocol("WM_DELETE_WINDOW", lambda: selection_window.destroy())
    root.mainloop()
