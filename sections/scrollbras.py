import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")


root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = tk.Text(root, height=8)
text.grid(row=0, column=0, sticky="ew")
text.insert("1.0", "Please enter a comment...")

text_scrool = ttk.Scrollbar(root, orient="vertical", command=text.yview)
text_scrool.grid(row=0, column=1, sticky="ns")
text["yscrollcommand"] = text_scrool.set

root.mainloop()