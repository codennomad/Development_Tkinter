import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

initial_value = tk.IntVar(value=20)
spin_box = tk.Spinbox( #or ttk.
    root, 
    from_=0, # or values=(5, 10, 15, 20, 25, 30),
    to=30,
    textvariable=initial_value,
    wrap=False
)

spin_box.pack()


root.mainloop()

