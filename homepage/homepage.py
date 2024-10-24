# homepage.py
import tkinter as tk
from homepage.submodules.mode_selection import create_mode_dropdown, create_parameters, create_save_button
from .submodules.logout.logout import logout

def show_homepage(username):
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    entries, default_params = create_parameters(frame)
    variable = create_mode_dropdown(frame, username, entries, default_params)
    create_save_button(frame, username, variable, entries)

    logout_button = tk.Button(frame, text="Logout", command=lambda: logout(root))
    logout_button.pack()

    root.mainloop()