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


def slct():
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
    
    def give_flepth():
        flepath = csv_listbox.get(csv_listbox.curselection())

    # THIS ONE CREATES A BUTTON THAT RUNS THE FUNCTION, SELECTING THE CURRENTLY SELECTED CSV FILE
    tk.Button(selection_window, text='Select CSV File', command=give_flepth).pack(pady=10)

    # Keep the tkinter main loop running
    selection_window.protocol("WM_DELETE_WINDOW", lambda: selection_window.destroy())
    root.mainloop()