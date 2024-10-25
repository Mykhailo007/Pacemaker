# homepage/submodules/user_actions.py
import tkinter as tk
import os
import json

class UserActions:
    def __init__(self, frame, username, variable, parameter_manager):
        self.frame = frame
        self.username = username
        self.variable = variable
        self.parameter_manager = parameter_manager
        self.create_save_button()

    def save_parameters(self):
        if not self.parameter_manager.validate_parameters():
            return
        mode = self.variable.get()
        current_params = self.parameter_manager.get_parameters()
        self.save_user_parameters(mode, current_params)
        print("Updated parameters:", current_params)

    def create_save_button(self):
        save_button = tk.Button(self.frame, text="Save Parameters", command=self.save_parameters)
        save_button.pack()

    def save_user_parameters(self, mode, params):
        user_dir = os.path.join("user_data", self.username)
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        
        filepath = os.path.join(user_dir, f"{mode}_parameters.json")
        with open(filepath, 'w') as file:
            json.dump(params, file)
