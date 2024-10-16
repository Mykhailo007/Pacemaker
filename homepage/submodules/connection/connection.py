import tkinter as tk

def check_connection(): 
    return "STABLE" 
 
def display_connection_status(frame): 
    status = check_connection() 
    label = tk.Label(frame, text=f"Connection: {status}", fg="red" if status != "STABLE" else "green") 
    label.pack(anchor="ne")
