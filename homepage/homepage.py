# homepage.py
import tkinter as tk
from tkinter import ttk
from homepage.submodules.mode_selection import create_mode_dropdown, create_parameters, create_save_button
from .submodules.logout.logout import logout
from ecg_test import display_ecg_graph

def check_connection():
    return "STABLE"
 
def display_connection_status(frame):
    status = check_connection()
    label = tk.Label(frame, text=f"Connection: {status}", fg="red" if status != "STABLE" else "green")
    label.pack(side="right", padx=10, pady=5)

def show_homepage(username):
    root = tk.Tk()
    
    # Create header frame for connection status
    header_frame = tk.Frame(root)
    header_frame.pack(fill="x")
    
    # Display connection in header
    display_connection_status(header_frame)
    
    # Create scrollable frame for parameters
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Create parameters in scrollable frame
    entries, default_params = create_parameters(scrollable_frame)
    
    # Create mode dropdown above scrollable area
    variable = create_mode_dropdown(root, username, entries, default_params)
    
    # Pack scrollable components
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Create button frame at bottom
    button_frame = tk.Frame(root)
    button_frame.pack(side="bottom", fill="x", pady=5)
    
    create_save_button(button_frame, username, variable, entries)
    
    ECG_button = tk.Button(button_frame, text="Show Graph", command=lambda: display_ecg_graph())
    ECG_button.pack(side="left", padx=5)
    
    logout_button = tk.Button(button_frame, text="Logout", command=lambda: logout(root))
    logout_button.pack(side="right", padx=5)
    
    # Add mouse wheel scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    root.mainloop()