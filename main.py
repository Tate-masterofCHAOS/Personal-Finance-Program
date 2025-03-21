#This is the menu, DON'T TOUCH IT! MY FILE!
#Vincent's code

from tkinter import *  # Import all Tkinter functions
from tkinter import ttk  # Import themed Tkinter widgets

from test import durg
from budgeting_and_income import budget_nd_income as cam
from income_and_expense import menu as bai
from create_account import create
from goal import goals as gls

# Makes a variable to end the code
ended = 0  # Initialize end to 0 to indicate the program is running

def main(ended):
    while ended == 0:
        # Create the main application window
        root = Tk()  
        root.title('Random')  # Set the window title

        # Functions that set the variables
        def budgeting_income():
            root.destroy()  # Close the current window
            Toplevel(durg())  # Create a new top-level window for the 'durg' function
            
        def check_account():
            root.destroy()  # Close the current window
            Toplevel(cam())  # Create a new top-level window for the 'menu' function

        def income_expense():
            root.destroy()  # Close the current window
            Toplevel(bai())  # Create a new top-level window for the 'bai' function

        def crt_accnt():
            root.destroy()  # Close the current window
            Toplevel(create())  # Create a new top-level window for the 'create' function

        def goals():
            root.destroy()  # Close the current window
            Toplevel(gls())  # Create a new top-level window for the 'create' function

        def end_program():
            nonlocal ended  # Use the nonlocal keyword to modify the outer variable
            ended = 1  # Set ended to 1 to indicate the program has ended
            root.destroy()  # Close the current window

        # Create a main frame inside the window with padding
        # Padding values: Left (3), Top (3), Right (12), Bottom (12)
        mainframe = ttk.Frame(root, padding="3 3 12 12")  
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Expand in all directions

        # Configure resizing behavior
        root.columnconfigure(0, weight=1)  # Allow column expansion
        root.rowconfigure(0, weight=1)  # Allow row expansion

        # Create buttons that print stuff
        button1 = ttk.Button(mainframe, text='Budgetting and Income', command=budgeting_income) # Budgeting and income function
        button1.grid(column=1, row=2, sticky=W)

        button2 = ttk.Button(mainframe, text='Check Account', command=check_account) # Check account function
        button2.grid(column=1, row=3, sticky=W)

        button3 = ttk.Button(mainframe, text='Income Expense Tracking', command=income_expense) # Income and expense tracking function
        button3.grid(column=2, row=2, sticky=W)

        button4 = ttk.Button(mainframe, text='Create an Account', command=crt_accnt) # Creating an account function
        button4.grid(column=2, row=3, sticky=W)

        button5 = ttk.Button(mainframe, text='Goals', command=goals) # Goals function
        button5.grid(column=3, row=2, sticky=W)

        button6 = ttk.Button(mainframe, text='Close', command=end_program) # Ends program
        button6.grid(column=2, row=8, sticky=N)

        # Create label for user instructions
        ttk.Label(mainframe, text='Please choose a function:').grid(column=2, row=1, sticky=W)

        # Create labels to display things
        ttk.Label(mainframe, textvariable="").grid(column=2, row=4, sticky=E)
        ttk.Label(mainframe, textvariable="").grid(column=2, row=5, sticky=E)
        ttk.Label(mainframe, textvariable="").grid(column=2, row=3, sticky=E)

        # Add padding to all child widgets inside 'mainframe' for better spacing
        for child in mainframe.winfo_children():  
            child.grid_configure(padx=5, pady=5)

        # Set the default window size (300x300 pixels)
        root.geometry('450x300')  

        # Allow the window to be resized in both width and height
        #root.resizable(True, True)  

        # Start the Tkinter event loop (keeps the window open and responsive)
        root.mainloop()
    return ended  # Return the end variable to indicate the program has ended

if __name__ == "__main__":
    while ended == 0:
        ended = main(ended)  # Call the main function to run the application
