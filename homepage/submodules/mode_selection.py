# homepage/submodules/mode_selection.py
import tkinter as tk
import json
import os

def save_user_parameters(username, mode, params):
    user_dir = os.path.join("user_data", username)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    
    filepath = os.path.join(user_dir, f"{mode}_parameters.json")
    with open(filepath, 'w') as file:
        json.dump(params, file)

def load_user_parameters(username, mode):
    filepath = os.path.join("user_data", username, f"{mode}_parameters.json")
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    else:
        return None

def create_mode_dropdown(frame, username, entries, default_params):
    modes = ["AOO", "VOO", "AAI", "VVI"]
    variable = tk.StringVar(frame)
    variable.set(modes[0])
    dropdown = tk.OptionMenu(frame, variable, *modes)
    dropdown.pack(anchor="nw")
    
    def on_mode_change(*args):
        mode = variable.get()
        params = load_user_parameters(username, mode)
        if params:
            for param, value in params.items():
                if param in entries:
                    entries[param].delete(0, tk.END)
                    entries[param].insert(0, str(value))
        else:
            for param, value in default_params.items():
                if param in entries:
                    entries[param].delete(0, tk.END)
                    entries[param].insert(0, str(value))
    
    variable.trace_add("write", on_mode_change)
    return variable

def create_parameters(frame):
    default_params = {
        "Lower Rate Limit": 20,
        "Upper Rate Limit": 100,
        "Atrial Amplitude": 2.5,
        "Atrial Pulse Width": 0.4,
        "Ventricular Amplitude": 3.0,
        "Ventricular Pulse Width": 0.6,
        "Atrial Refactory Period": 10,
        "Ventricular Refactory Period": 15
    }

    upper_limits = {
        "Lower Rate Limit": 50,
        "Upper Rate Limit": 200,
        "Atrial Amplitude": 5.0,
        "Atrial Pulse Width": 1.0,
        "Ventricular Amplitude": 5.5,
        "Ventricular Pulse Width": 1.2,
        "Atrial Refactory Period": 20,
        "Ventricular Refactory Period": 30
    }

    entries = {}
    for param, value in default_params.items():
        param_label = tk.Label(frame, text=param)
        param_label.pack()
        entry = tk.Entry(frame)
        entry.insert(0, str(value))
        entry.pack()

        def validate_input(value, param=param):
            try:
               if float(value) > upper_limits[param]:
               messagebox.showerror("Input Error", f"{param} cannot exceed {upper_limits[param]}")
                    entry.delete(0, tk.END)
                    entry.insert(0, str(upper_limits[param]))
            except ValueError:
                pass 

        entry.bind("<FocusOut>", lambda event, param=param: validate_input(entry.get(), param)) 

        entries[param] = entry

    return entries, default_params

def create_save_button(frame, username, variable, entries):
    def save_params():
        mode = variable.get()
        current_params = {param: float(entry.get()) for param, entry in entries.items()}
        save_user_parameters(username, mode, current_params)
    
    save_button = tk.Button(frame, text="Save Parameters", command=save_params)
    save_button.pack()
