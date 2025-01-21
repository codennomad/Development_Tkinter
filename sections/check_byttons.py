import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")


#root.grid_columnconfigure(0, weight=1)
#root.grid_rowconfigure(0, weight=1)

selected_option = tk.StringVar()

def print_current_option():
    print(selected_option.get())
    
check = ttk.Checkbutton(
    root,
    text="Check me!",
    variable=selected_option,
    command=print_current_option,
    onvalue="On",
    offvalue="Off"
)

check.pack()

#check_button = ttk.Checkbutton(root, text="Check me!")
#check_button.pack()

root.mainloop()