import tkinter as tk

def create_mode_dropdown(frame): 
    modes = ["AOO", "VOO", "AAI", "VVI"] 
    variable = tk.StringVar(frame) 
    variable.set(modes[0]) 
    dropdown = tk.OptionMenu(frame, variable, *modes) 
    dropdown.pack(anchor="nw") 
    return variable 
