# homepage.py
import tkinter as tk
from tkinter import ttk
from submodules.mode_selection import create_mode_dropdown, create_parameters, create_save_button
from submodules.logout.logout import logout
from ecg_test import display_ecg_graph

import wmi
import io
import re
from contextlib import redirect_stdout

def check_connection():
    """Check for hardware connection and return status"""
    try:
        # Initialize WMI
        c = wmi.WMI()
        serial_value = -1
        
        # Capture output
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            # Query hardware information
            for item in c.Win32_PhysicalMedia():
                print(item)
            for drive in c.Win32_DiskDrive():
                print(drive)
            for disk in c.Win32_LogicalDisk():
                print(disk)
        
        # Get output text
        output_text = captured_output.getvalue()
        
        # Search for hardware ID pattern
        pattern = r'\b[0-9A-Fa-f]{8}&\d&\d{12}\b'
        match = re.search(pattern, output_text)
        
        if match:
            serial_value = match.group(0)
        
        # Check for specific hardware
        if "SEGGER" in output_text:
            return "STABLE"
        else:
            return "DISCONNECTED"
            
    except Exception as e:
        print(f"Error checking connection: {e}")
        return "ERROR"

def display_connection_status(frame):
    """Display connection status in frame"""
    status = check_connection()
    label = tk.Label(frame, text=f"Connection: {status}", fg="red" if status != "STABLE" else "green")
    label.pack(anchor="ne")


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