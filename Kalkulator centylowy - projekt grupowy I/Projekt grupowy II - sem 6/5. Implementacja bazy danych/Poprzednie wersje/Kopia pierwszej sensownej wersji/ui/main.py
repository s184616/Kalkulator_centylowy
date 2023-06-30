import tkinter

from ui import *
import global_variables
from db_connection import *

# Importing module
import mysql.connector

if __name__ == "__main__":
    """
    Main function, create main window and call create_user_interface function
    
    Function create_user_interface is in ui.py file, and as an argument it takes main window
    create 
    """

    # create main window
    main = tk.Tk()
    main.title("Kalkulator centylowy")

    # get screen width and height
    width = main.winfo_screenwidth()
    height = main.winfo_screenheight()

    # setting up window size
    # main.geometry(f"{width}x{height}") # set window size to screen size
    main.geometry("600x700")  # set window size to 1100x800

    # background color
    main.configure(bg=global_variables.background_color)  # setting background color`

    create_main_menu(main)

    # running main window
    main.mainloop()

