import tkinter as tk

my_window = tk.Tk()
my_window.title("Demo")
my_window.geometry("300x300")


def change_text():
    my_button["text"] = "I've been clicked!"
    my_button['state'] = 'disabled'


my_button = tk.Button(my_window, text="Submit", command=change_text)
my_button.pack()
my_window.mainloop()