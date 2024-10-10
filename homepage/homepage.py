import tkinter as tk
from .submodules.connection import display_connection_status
from .submodules.mode_selection import create_mode_dropdown
from .submodules.parameters import create_parameters
from .submodules.user_actions import create_save_button

 
def show_homepage(): 
    root = tk.Tk() 
    root.title("Pacemaker Settings")
    root.state('zoomed')  # Maximize window

 
    top_frame = tk.Frame(root) 
    top_frame.pack(pady=10) 
 
    param_frame = tk.Frame(root) 
    param_frame.pack(pady=10) 
 
    display_connection_status(top_frame) 
    mode_var = create_mode_dropdown(top_frame) 
 
    entries = create_parameters(param_frame) 
    create_save_button(root, entries) 

    # Logout button
    logout_button = tk.Button(root, text="Logout", font=("Arial", 14), command=lambda: logout_user(root))
    logout_button.pack(pady=20)
 
    root.mainloop() 

def logout_user(homepage_window):
    homepage_window.destroy()  # Close the homepage window
    from main import start_login  # Import here to avoid circular dependency issues
    start_login()  # Go back to login screen