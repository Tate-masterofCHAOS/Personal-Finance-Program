#This is the menu, DON'T TOUCH IT! MY FILE!
#Vincent's code
import os
import tkinter as tk
from tkinter import *  # Import all Tkinter functions
from tkinter import ttk  # Import themed Tkinter widgets
from datetime import datetime
import pandas as pd

from income_and_expense import Baimenu as bai
from goal import Gmenu as gls
from goal import Gset as gs
from chart import Charts  # Import the Charts class from slct_prfl.py
from create_account import CAmenu  # Import the CAmenu class from create_account.py
from check_account import Chk  # Import the Chk class from check_account.py

# Makes a variable to end the code
ended = 0  # Initialize end to 0 to indicate the program is running

def main(ended):
    root = Tk()  # Always create a new Tkinter root window
    root.title('Main Menu')  # Set the title of the window

    # Clear any existing widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    def check_account():
        root.destroy()  # Close the current window
        new_root = Tk()  # Create a new Tkinter root window
        Chk(new_root)  # Pass the new root to new function
        nonlocal ended
        ended = 1

    def income_expense():
        root.destroy()  # Close the current window
        new_root = Tk()  # Create a new Tkinter root window
        bai(new_root)  # Pass the new root to new function
        nonlocal ended
        ended = 1

    def crt_accnt():
        root.destroy()  # Close the current window
        new_root = Tk()  # Create a new Tkinter root window
        CAmenu(new_root)  # Pass the new root window to CAmenu
        nonlocal ended
        ended = 1

    def goals_edit():
        root.destroy()  # Close the current window
        new_root = Tk()  # Create a new Tkinter root window
        gs(new_root)  # Pass the new root to new function
        nonlocal ended
        ended = 1

    def goals_view():
        root.destroy()  # Close the current window
        new_root = Tk()  # Create a new Tkinter root window
        gls(new_root)  # Pass the new root to new function
        nonlocal ended
        ended = 1

    def goals():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Label(goals_frame, text='Goals').grid(column=3, row=0, sticky=W)
        ttk.Label(goals_frame, text='').grid(column=1, row=0, sticky=W, columnspan=2)
        ttk.Label(goals_frame, text='').grid(column=1, row=1, sticky=W, columnspan=2)
        ttk.Button(goals_frame, text='Check goal', command=goals_view).grid(column=3, row=1, sticky=W)
        ttk.Button(goals_frame, text='Edit goal', command=goals_edit).grid(column=4, row=1, sticky=W)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def end_program():
        root.destroy()  # Close the current window
        nonlocal ended
        ended = 1

    def chrts():
        root.destroy()  # Close the current window
        new_root = Tk()  # Create a new Tkinter root window
        Charts(new_root)  # Pass the new root to new function
        nonlocal ended
        ended = 1

    # Create a main frame inside the window with padding
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    # Configure resizing behavior
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create buttons for the main menu
    ttk.Button(mainframe, text='Chart', command=chrts).grid(column=1, row=2, sticky=W)
    ttk.Button(mainframe, text='Check Account', command=check_account).grid(column=1, row=3, sticky=W)
    ttk.Button(mainframe, text='Income Expense Tracking', command=income_expense).grid(column=2, row=2, sticky=W)
    ttk.Button(mainframe, text='Create an Account', command=crt_accnt).grid(column=2, row=3, sticky=W)
    ttk.Button(mainframe, text='Goals', command=goals).grid(column=3, row=2, sticky=W)
    ttk.Button(mainframe, text='Close', command=end_program).grid(column=2, row=8, sticky=N)

    # Add a label for user instructions
    ttk.Label(mainframe, text='Please choose a function:').grid(column=2, row=1, sticky=W)

    # Add padding to all child widgets inside 'mainframe'
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    # Set the default window size
    root.geometry('450x300')

    # Start the Tkinter event loop
    root.mainloop()
    return ended

if __name__ == "__main__":
    while ended == 0:
        ended = main(ended)  # Call the main function to run the application
