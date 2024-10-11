import tkinter as tk

def save_parameters(entries): 
    updated_params = {param: entry.get() for param, entry in entries.items()} 
    print("Updated parameters:", updated_params) 
 
def create_save_button(frame, entries): 
    button = tk.Button(frame, text="Save", command=lambda: save_parameters(entries)) 
    button.pack() 
