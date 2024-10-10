import tkinter as tk
from .submodules.connection import display_connection_status
from .submodules.mode_selection import create_mode_dropdown
from .submodules.parameters import create_parameters
from .submodules.user_actions import create_save_button

 
def show_homepage(): 
    root = tk.Tk() 
    root.title("Pacemaker Settings") 
 
    top_frame = tk.Frame(root) 
    top_frame.pack(pady=10) 
 
    param_frame = tk.Frame(root) 
    param_frame.pack(pady=10) 
 
    display_connection_status(top_frame) 
    mode_var = create_mode_dropdown(top_frame) 
 
    entries = create_parameters(param_frame) 
    create_save_button(root, entries) 
 
    root.mainloop() 
