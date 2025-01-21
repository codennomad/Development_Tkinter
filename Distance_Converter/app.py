import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here.")

def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass

root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30,15))
main.grid()

metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

metres_label.grid(column=0, row=0, sticky="W") #metres_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
metres_input.grid(column=1, row=0, sticky="EW") #metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W") #feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
feet_display.grid(column=1, row=1, sticky="EW") #feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW") #calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)


for child in main.winfo_children():
    child.grid_configure(padx=7, pady=7)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)


root.mainloop()

