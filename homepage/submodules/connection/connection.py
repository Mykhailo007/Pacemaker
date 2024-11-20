import tkinter as tk
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
    label = tk.Label(frame, text=f"Connection: {status}", 
                     fg="red" if status != "STABLE" else "green")
    label.pack(anchor="ne")
