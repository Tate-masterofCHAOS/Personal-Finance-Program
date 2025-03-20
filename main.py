#This is the menu, DON'T TOUCH IT! MY FILE!
#Vincent's code

from tkinter import *  # Import all Tkinter functions
from tkinter import ttk  # Import themed Tkinter widgets

# Create the main application window
root = Tk()  
root.title('Random')  # Set the window title

# Make variables that can change and show things through .set()
print1 = StringVar()
print2 = StringVar()

# Functions that set the variables
def printer1():
    print1.set('Bleurgh!')
def printer2():
    print2.set('Goodbye!')

# Create a main frame inside the window with padding
# Padding values: Left (3), Top (3), Right (12), Bottom (12)
mainframe = ttk.Frame(root, padding="3 3 12 12")  
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Expand in all directions

# Configure resizing behavior
root.columnconfigure(0, weight=1)  # Allow column expansion
root.rowconfigure(0, weight=1)  # Allow row expansion

# Create buttons that print stuff
button1 = ttk.Button(mainframe, text='Say bleurgh', command=printer1).grid(column=1, row=2, sticky=E)
button2 = ttk.Button(mainframe, text='Say goodbye', command=printer2).grid(column=1, row=3, sticky=E)

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
