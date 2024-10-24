# homepage.py
import tkinter as tk
from homepage.submodules.mode_selection import create_mode_dropdown, create_parameters, create_save_button
from .submodules.logout.logout import logout

def check_connection():
    return "STABLE"
 
def display_connection_status(frame):
    status = check_connection()
    label = tk.Label(frame, text=f"Connection: {status}", fg="red" if status != "STABLE" else "green")
    label.pack(anchor="ne")

def show_homepage(username):
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    display_connection_status(frame)
    entries, default_params = create_parameters(frame)
    variable = create_mode_dropdown(frame, username, entries, default_params)
    create_save_button(frame, username, variable, entries)

    logout_button = tk.Button(frame, text="Logout", command=lambda: logout(root))
    logout_button.pack()

    root.mainloop()