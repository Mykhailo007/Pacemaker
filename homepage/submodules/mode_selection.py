# homepage/submodules/mode_selection.py
import tkinter as tk
import json
import os

class ModeSelection:
    def __init__(self, frame, username):
        self.frame = frame
        self.username = username
        self.entries, self.default_params = self.create_parameters()
        self.variable = self.create_mode_dropdown()

    def save_user_parameters(self, mode, params):
        user_dir = os.path.join("user_data", self.username)
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        
        filepath = os.path.join(user_dir, f"{mode}_parameters.json")
        with open(filepath, 'w') as file:
            json.dump(params, file)

    def load_user_parameters(self, mode):
        filepath = os.path.join("user_data", self.username, f"{mode}_parameters.json")
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                return json.load(file)
        return None

    def create_mode_dropdown(self):
        modes = ["AAT", "VVT", "AOO", "AAI", "VOO", "VVI", "VDD", "DOO", "DDI", "DDD", "AOOR", "AAIR", "VOOR", "VVIR", "VDDR", "DOOR", "DDIR", "DDDR"]
        variable = tk.StringVar(self.frame)
        variable.set(modes[0])
        dropdown = tk.OptionMenu(self.frame, variable, *modes)
        dropdown.pack(anchor="nw")
        
        def on_mode_change(*args):
            mode = variable.get()
            params = self.load_user_parameters(mode)
            if params:
                for param, value in params.items():
                    if param in self.entries:
                        self.entries[param].delete(0, tk.END)
                        self.entries[param].insert(0, str(value))
            else:
                for param, value in self.default_params.items():
                    if param in self.entries:
                        self.entries[param].delete(0, tk.END)
                        self.entries[param].insert(0, str(value))
        
        variable.trace_add("write", on_mode_change)
        return variable

    def create_parameters(self):
        default_params = {
            "Lower Rate Limit": 60, 
            "Upper Rate Limit": 120, 
            "Maximum Sensor Rate": 120,
            "Atrial Amplitude": 2.5, 
            "Atrial Pulse Width": 0.4, 
            "Ventricular Amplitude": 3.0, 
            "Ventricular Pulse Width": 0.6,
            "Atrial Sensitivity": 0.75,
            "Ventricular Sensitivity": 2.5,
            "Atrial Refactory Period": 250,
            "Ventricular Refactory Period": 320,
            "PVARP": 250,
            "PVARP Extension": 0,
            "Hysteresis": 0,
            "Rate Smoothing": 0,
            "ATR Duration": 20,
            "ATR Fallback Mode": 0,
            "ATR Fallback Time": 1,
            "Activity Threshold": 3,
            "Reaction Time": 30,
            "Response Factor": 8,
            "Recovery Time": 5
        }

        entries = {}
        for param, value in default_params.items():
            param_label = tk.Label(self.frame, text=param)
            param_label.pack()

            entry = tk.Entry(self.frame)
            entry.insert(0, str(value))
            entry.pack()

            entries[param] = entry

        return entries, default_params

    def create_save_button(self):
        def save_params():
            mode = self.variable.get()
            current_params = {param: float(entry.get()) for param, entry in self.entries.items()}
            self.save_user_parameters(mode, current_params)
        
        save_button = tk.Button(self.frame, text="Save Parameters", command=save_params)
        save_button.pack()
