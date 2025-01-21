import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")


selected_option = tk.StringVar()


    
option_one = ttk.Radiobutton(
    root,
    text="option 1",
    variable=selected_option,
    value="First option"
)

option_two = ttk.Radiobutton(
    root,
    text="option 2",
    variable=selected_option,
    value="second option"
)

option_three = ttk.Radiobutton(
    root,
    text="option 3",
    variable=selected_option,
    value="Third option"
)

option_one.pack()
option_two.pack()
option_three.pack()

root.mainloop()