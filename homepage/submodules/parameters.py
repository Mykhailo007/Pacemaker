import tkinter as tk

def create_parameters(frame): 
    params = { 
        "Lower Rate Limit": 20, 
        "Upper Rate Limit": 100, 
        "Atrial Amplitude": 2.5, 
        "Atrial Pulse Width": 0.4, 
        "Ventricular Amplitude": 3.0, 
        "Ventricular Pulse Width": 0.6,
        "Atrial Refactory Period": 10,
        "Ventricular Refactory Period": 15
    } 
 
    entries = {} 
    for param, value in params.items(): 
        param_label = tk.Label(frame, text=param) 
        param_label.pack() 
        entry = tk.Entry(frame) 
        entry.insert(0, str(value)) 
        entry.pack() 
        entries[param] = entry 
 
    return entries 
