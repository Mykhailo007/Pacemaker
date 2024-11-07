# homepage/submodules/mode_selection.py
import tkinter as tk
import json
import os
from homepage.submodules.parameters import ParameterManager

class ModeSelection:
    def __init__(self, frame, username):
        self.frame = frame
        self.username = username
        self.parameter_manager = ParameterManager(self.frame)
        self.entries = self.parameter_manager.entries
        self.default_params = self.parameter_manager.default_params
        self.variable = self.create_mode_dropdown()

    def save_user_parameters(self, mode, params):
        user_dir = os.path.join("user_data", self.username)
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        
        filepath = os.path.join(user_dir, f"{mode}_parameters.json")
        with open(filepath, 'w') as file:
            json.dump(params, file)

    def load_user_parameters(self, mode):
        user_dir = os.path.join("user_data", self.username)
        filepath = os.path.join(user_dir, f"{mode}_parameters.json")
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                return json.load(file)
        return None

    def create_mode_dropdown(self):
        modes = ["AOO", "VOO", "AAI", "VVI"]
        variable = tk.StringVar(self.frame)
        variable.set(modes[0])
        dropdown = tk.OptionMenu(self.frame, variable, *modes)
        dropdown.pack(anchor="nw")
        
        def on_mode_change(*args):
            mode = variable.get()
            params = self.load_user_parameters(mode)
            if params:
                self.parameter_manager.set_parameters(params)
            else:
                self.parameter_manager.set_parameters(self.default_params)
        
        variable.trace_add("write", on_mode_change)
        return variable
