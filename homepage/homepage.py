# homepage/homepage.py
import tkinter as tk
from tkinter import ttk
from homepage.submodules.connection.connection import ConnectionStatus
from homepage.submodules.mode_selection import ModeSelection
from homepage.submodules.user_actions import UserActions
from homepage.submodules.logout.logout import Logout
from homepage.submodules.ecg import ECGGraph
import wmi
import io
import re
from contextlib import redirect_stdout

class Homepage:
    def __init__(self, username, show_login_page_callback):
        self.username = username
        self.show_login_page_callback = show_login_page_callback
        self.frame = None
        self.ecg_graph = ECGGraph()  # Instantiate ECGGraph

    def check_connection(self):
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

    def display_connection_status(self):
        """Display connection status in frame"""
        status = self.check_connection()
        label = tk.Label(self.frame, text=f"Connection: {status}", fg="red" if status != "STABLE" else "green")
        label.pack(anchor="ne")

    def show(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        # Create header frame for connection status
        header_frame = tk.Frame(self.frame)
        header_frame.pack(fill="x")
        
        # Display connection in header
        self.display_connection_status()
        
        # Create scrollable frame for parameters
        canvas = tk.Canvas(self.frame)
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create ModeSelection instance
        mode_selection = ModeSelection(scrollable_frame, self.username)
        
        # Pack scrollable components
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Create button frame at bottom
        button_frame = tk.Frame(self.frame)
        button_frame.pack(side="bottom", fill="x", pady=5)
        
        mode_selection.create_save_button()
        
        self.create_ecg_button(button_frame)
        
        logout_button = tk.Button(button_frame, text="Logout", command=lambda: self.logout.logout(root))
        logout_button.pack(side="right", padx=5)
        
        # Add mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def create_ecg_button(self, frame):
        ecg_button = tk.Button(frame, text="Show Graph", command=self.ecg_graph.display)
        ecg_button.pack(side="left", padx=5)