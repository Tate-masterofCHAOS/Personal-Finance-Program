import os

from tkinter import *  # Import all Tkinter functions
from tkinter import ttk  # Import themed Tkinter widgets

def menu():
    # Create the main application window
    root = Tk()  
    root.title('Random')  # Set the window title

    # Make variables that can change and show things through .set()
    print1 = StringVar()
    print2 = StringVar()

    # Functions that set the variables
    def printer1():
        print1.set('Durg!')
        
    def printer2():
        print2.set('Blurg!')

    def printer3():
        root.destroy()  # Close the current window
        main_file_path = os.path.join(os.path.dirname(__file__), 'main.py')
        Toplevel(os.system(f'python "{main_file_path}"'))

    # Create a main frame inside the window with padding
    # Padding values: Left (3), Top (3), Right (12), Bottom (12)
    mainframe = ttk.Frame(root, padding="3 3 12 12")  
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Expand in all directions

    # Configure resizing behavior
    root.columnconfigure(0, weight=1)  # Allow column expansion
    root.rowconfigure(0, weight=1)  # Allow row expansion

    # Create buttons that print stuff
    button1 = ttk.Button(mainframe, text='Say durg', command=printer1).grid(column=1, row=2, sticky=E) #Instead of printer1, use the function that the user asked for, make a menu on those files too
    button2 = ttk.Button(mainframe, text='Say blurg', command=printer2).grid(column=1, row=3, sticky=E)
    button3 = ttk.Button(mainframe, text='Back to menu', command=printer3).grid(column=1, row=4, sticky=E)

    # Create label for user instructions
    ttk.Label(mainframe, text='Please choose a function:').grid(column=2, row=1, sticky=N)

    # Create labels to display things
    ttk.Label(mainframe, textvariable=print1).grid(column=2, row=2, sticky=E)
    ttk.Label(mainframe, textvariable=print2).grid(column=2, row=3, sticky=E)

    # Add padding to all child widgets inside 'mainframe' for better spacing
    for child in mainframe.winfo_children():  
        child.grid_configure(padx=5, pady=5)

    # Set the default window size (300x300 pixels)
    root.geometry('300x300')  

    # Allow the window to be resized in both width and height
    root.resizable(True, True)  

    # Start the Tkinter event loop (keeps the window open and responsive)
    root.mainloop()