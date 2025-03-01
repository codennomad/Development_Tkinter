import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")


selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekday["state"] = "readonly" #normal
weekday.pack()

def handle_selection(event):
    print("Today is", selected_weekday.get())
    #print("But we're gonna change it to Friday.")
    #selected_weekday.set("Friday") - change the chosen day to Friday
    print(weekday.current()) # prints out the current value as an index


weekday.bind("<<ComboboxSelected>>", handle_selection)

root.mainloop()

print(selected_weekday.get(), "was selected")