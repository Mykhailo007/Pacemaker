import tkinter as tk

def create_parameters(frame): 
    params = { 
        "Lower Rate Limit": 60, 
        "Upper Rate Limit": 120, 
        "Maximum Sensor Rate": 120,
        "Atrial Amplitude": 2.5, 
        "Atrial Pulse Width": 0.4, 
        "Ventricular Amplitude": 3.0, 
        "Ventricular Pulse Width": 0.6,
        "Atrial Sensitivity": 0.75,
        "Ventricular Sensitivity": 2.5,
        "Atrial Refactory Period": 250,
        "Ventricular Refactory Period": 320,
        "PVARP": 250,
        "PVARP Extension": 0,
        "Hysteresis": 0,
        "Rate Smoothing": 0,
        "ATR Duration": 20,
        "ATR Fallback Mode": 0,
        "ATR Fallback Time": 1,
        "Activity Threshold": 3,
        "Reaction Time": 30,
        "Response Factor": 8,
        "Recovery Time": 5
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
