# This is the menu, DON'T TOUCH IT! MY FILE!
# Vincent's code
import os
import tkinter as tk
from tkinter import ttk

from income_and_expense import Baimenu as bai
from goal import Gmenu as gls, Gset as gs
from chart import Charts
from create_account import CAmenu
from check_account import Chk
from slct_prfl import Slct
from change_currency import Cc
from budgetting import Budge, Budge_shw


# Global variable to track program state
ended = 0  # Initialize to 0 to indicate the program is running
restart = 0

def main():
    try:
        root.destroy
    except:
        pass
    global ended  # Declare 'ended' as a global variable
    root = tk.Tk()  # Create the main Tkinter root window
    root.title('Main Menu')  # Set the title of the window

    # Clear any existing widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    def check_account():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window

        def return_to_menu():
            main()  # Restart the main menu

        profile_window = tk.Tk()  # Create a new Tkinter root window for profile selection
        profile_selector = Slct(profile_window, return_to_menu)  # Pass the callback to the Slct class
        profile_window.wait_window()  # Wait until the profile selection window is closed

        # Retrieve the selected file path
        file_path = profile_selector.get_selected_file()
        if not file_path:
            tk.messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            main()  # Restart the main menu if no file is selected
            return

        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        Chk(new_root, file_path)  # Pass the file_path to the Chk class
        ended = 1

    def income_expense():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window

        def return_to_menu():
            main()  # Restart the main menu

        profile_window = tk.Tk()  # Create a new Tkinter root window for profile selection
        profile_selector = Slct(profile_window, return_to_menu)  # Pass the callback to the Slct class
        profile_window.wait_window()  # Wait until the profile selection window is closed

        # Retrieve the selected file path
        file_path = profile_selector.get_selected_file()
        if not file_path:
            tk.messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            main()  # Restart the main menu if no file is selected
            return

        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        bai(new_root, file_path)  # Pass the file_path to the Baimenu class
        ended = 1

    def crt_accnt():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        CAmenu(new_root)  # Pass the file_path to the CAmenu class
        ended = 1

    def goals_edit():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window

        def return_to_menu():
            main()  # Restart the main menu

        profile_window = tk.Tk()  # Create a new Tkinter root window for profile selection
        profile_selector = Slct(profile_window, return_to_menu)  # Pass the callback to the Slct class
        profile_window.wait_window()  # Wait until the profile selection window is closed

        # Retrieve the selected file path
        file_path = profile_selector.get_selected_file()
        if not file_path:
            tk.messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            main()  # Restart the main menu if no file is selected
            return

        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        gs(new_root, file_path)  # Pass the file_path to the Gset class
        ended = 1

    def goals_view():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window

        def return_to_menu():
            main()  # Restart the main menu

        profile_window = tk.Tk()  # Create a new Tkinter root window for profile selection
        profile_selector = Slct(profile_window, return_to_menu)  # Pass the callback to the Slct class
        profile_window.wait_window()  # Wait until the profile selection window is closed

        # Retrieve the selected file path
        file_path = profile_selector.get_selected_file()
        if not file_path:
            tk.messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            main()  # Restart the main menu if no file is selected
            return

        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        gls(new_root, file_path)  # Pass the file_path to the Gset class
        ended = 1

    def goals():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Button(goals_frame, text='Check goal', command=goals_view).grid(column=0, row=1)
        ttk.Button(goals_frame, text='Edit goal', command=goals_edit).grid(column=1, row=1)
        ttk.Button(goals_frame, text='Menu', command=restart).grid(column=2, row=1)

        ttk.Label(goals_frame, text='Goals').grid(column=0, row=0, columnspan=2, pady = 20, padx=20)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def restart():
        current_file_path = os.path.abspath(__file__)

    def end_program():
        global ended  # Declare 'ended' as a global variable
        if not ended:  # Check if the program has not already ended
            root.destroy()  # Close the current window
            ended = 1  # Mark the program as ended

    def chrts():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window

        def return_to_menu():
            main()  # Restart the main menu

        profile_window = tk.Tk()  # Create a new Tkinter root window for profile selection
        profile_selector = Slct(profile_window, return_to_menu)  # Pass the callback to the Slct class
        profile_window.wait_window()  # Wait until the profile selection window is closed

        # Retrieve the selected file path
        file_path = profile_selector.get_selected_file()
        if not file_path:
            tk.messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            main()  # Restart the main menu if no file is selected
            return

        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        Charts(new_root, file_path)  # Pass the file_path to the Charts class
        ended = 1

    def Chnge_curr():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window

        def return_to_menu():
            main()  # Restart the main menu

        profile_window = tk.Tk()  # Create a new Tkinter root window for profile selection
        profile_selector = Slct(profile_window, return_to_menu)  # Pass the callback to the Slct class
        profile_window.wait_window()  # Wait until the profile selection window is closed

        # Retrieve the selected file path
        file_path = profile_selector.get_selected_file()
        if not file_path:
            tk.messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            main()  # Restart the main menu if no file is selected
            return

        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        Cc(new_root, file_path)  # Pass the file_path to the Charts class
        ended = 1
    
    def budgt_shw():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window

        def return_to_menu():
            main()  # Restart the main menu

        profile_window = tk.Tk()  # Create a new Tkinter root window for profile selection
        profile_selector = Slct(profile_window, return_to_menu)  # Pass the callback to the Slct class
        profile_window.wait_window()  # Wait until the profile selection window is closed

        # Retrieve the selected file path
        file_path = profile_selector.get_selected_file()
        if not file_path:
            tk.messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            main()  # Restart the main menu if no file is selected
            return

        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        Budge_shw(new_root, file_path)  # Pass the file_path to the Charts class
        ended = 1

    def budgt():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window

        def return_to_menu():
            main()  # Restart the main menu

        profile_window = tk.Tk()  # Create a new Tkinter root window for profile selection
        profile_selector = Slct(profile_window, return_to_menu)  # Pass the callback to the Slct class
        profile_window.wait_window()  # Wait until the profile selection window is closed

        # Retrieve the selected file path
        file_path = profile_selector.get_selected_file()
        if not file_path:
            tk.messagebox.showerror("Error", "No file selected. Returning to the main menu.")
            main()  # Restart the main menu if no file is selected
            return

        # After the profile selection window is closed, create the new window
        new_root = tk.Tk()
        Budge(new_root, file_path)  # Pass the file_path to the Charts class
        ended = 1

    def budgt_menu():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Button(goals_frame, text='Check budget catagories', command=budgt_shw).grid(column=0, row=1)
        ttk.Button(goals_frame, text='Edit budget catagories', command=budgt).grid(column=1, row=1)

        ttk.Label(goals_frame, text='Goals').grid(column=0, row=0, columnspan=2, pady = 20, padx=20)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    

    # Create a main frame inside the window with padding
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    # Configure resizing behavior
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create buttons for the main menu
    ttk.Button(mainframe, text='Chart', command=chrts).grid(column=1, row=2)
    ttk.Button(mainframe, text='Check Account Total', command=check_account).grid(column=1, row=3)
    ttk.Button(mainframe, text='Income Expense Tracking', command=income_expense).grid(column=2, row=2)
    ttk.Button(mainframe, text='Create an Account', command=crt_accnt).grid(column=2, row=3)
    ttk.Button(mainframe, text='Goals', command=goals).grid(column=3, row=2)
    ttk.Button(mainframe, text='Change currency', command=Chnge_curr).grid(column=3, row=3)
    ttk.Button(mainframe, text='Budgetting', command=budgt_menu).grid(column=1, row=4)
    ttk.Button(mainframe, text='Close', command=end_program).grid(column=2, row=8)

    # Add a label for user instructions
    ttk.Label(mainframe, text='Please choose a function:').grid(column=2, row=1)

    # Add padding to all child widgets inside 'mainframe'
    for child in mainframe.winfo_children():
        child.grid_configure(padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()
    return ended, restart


if __name__ == "__main__":
    if restart == 1:
        restart = 0
        ended, restart = main()
    while ended == 0:
        ended, restart = main()  # Call the main function to run the application