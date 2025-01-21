import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

class DistanceConverter(tk.Tk):
    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        
        self.title("Distance Converter")
        self.frames = dict()
        
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")
        
        
        for FrameClass in (FeetToMetres, MetresToFeet):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
            
        self.show_frame(MetresToFeet)
        '''This code binds the "Enter" key (<Return>) and the "Keypad Enter" key (<KP_Enter>)  
        to trigger the calculation method when either key is pressed. However, this functionality only  
        works after the user interacts with the "Calculate" or "Switch" buttons, as these interactions  
        set the focus required for the key bindings to take effect. Without button interaction, pressing  
        "Enter" alone will not initiate the calculation. This design improves user input handling by  
        providing better control, while ensuring a deliberate action to activate the function.  
'''
    
    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()
        
class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller , **kwargs):
        super().__init__(container, **kwargs)
        
        self.feet_value = tk.StringVar(value="Feet shown here.")
        self.metres_value = tk.StringVar()
        
        metres_label = ttk.Label(self, text="Metres:")
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Segoe UI", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        
        metres_label.grid(column=0, row=0, sticky="W") 
        metres_input.grid(column=1, row=0, sticky="EW") 
        metres_input.focus()

        feet_label.grid(column=0, row=1, sticky="W") 
        feet_display.grid(column=1, row=1, sticky="EW") 

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_page_button = ttk.Button(
            self,
            text="Switch to feet conversion",
            command=lambda: controller.show_frame(FeetToMetres)
        )
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")
        
        for child in self.winfo_children():
            child.grid_configure(padx=7, pady=7)
      
        
    def calculate(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass
        
        
       
class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller , **kwargs):
        super().__init__(container, **kwargs)
        
        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar()
        
        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Segoe UI", 15))
        metres_label = ttk.Label(self, text="Metres:")
        metres_display = ttk.Label(self, textvariable=self.metres_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to metres conversion",
            command=lambda: controller.show_frame(MetresToFeet)
        )
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")
        
        
        feet_label.grid(column=0, row=0, sticky="W") 
        feet_input.grid(column=1, row=0, sticky="EW")
        feet_input.focus() 
        
        metres_label.grid(column=0, row=1, sticky="W") 
        metres_display.grid(column=1, row=1, sticky="EW") 


        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        
        for child in self.winfo_children():
            child.grid_configure(padx=7, pady=7)
      
        
    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            metres = feet / 3.28084
            self.metres_value.set(f"{metres:.3f}")
        except ValueError:
            pass
        
root = DistanceConverter()
font.nametofont("TkDefaultFont").configure(size=15)
root.columnconfigure(0, weight=1)
root.mainloop()