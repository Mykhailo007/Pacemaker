import tkinter as tk
from tkinter import messagebox

class ParameterManager:
    def __init__(self, frame):
        self.frame = frame
        self.default_params = {
            "Lower Rate Limit": 20,
            "Upper Rate Limit": 100,
            "Atrial Amplitude": 2.5,
            "Atrial Pulse Width": 0.4,
            "Ventricular Amplitude": 3.0,
            "Ventricular Pulse Width": 0.6,
            "Atrial Refactory Period": 10,
            "Ventricular Refactory Period": 15
        }
        self.max_values = {
            "Lower Rate Limit": 50,
            "Upper Rate Limit": 200,
            "Atrial Amplitude": 5.0,
            "Atrial Pulse Width": 1.0,
            "Ventricular Amplitude": 5.5,
            "Ventricular Pulse Width": 1.2,
            "Atrial Refactory Period": 20,
            "Ventricular Refactory Period": 30
        }
        self.entries = self.create_parameters()

    def create_parameters(self):
        entries = {}
        for param, value in self.default_params.items():
            param_label = tk.Label(self.frame, text=param)
            param_label.pack()

            entry = tk.Entry(self.frame)
            entry.insert(0, str(value))
            entry.pack()

            entries[param] = entry

        return entries

    def get_parameters(self):
        return {param: float(entry.get()) for param, entry in self.entries.items()}

    def set_parameters(self, params):
        for param, value in params.items():
            if param in self.entries:
                self.entries[param].delete(0, tk.END)
                self.entries[param].insert(0, str(value))

    def validate_parameters(self):
        for param, entry in self.entries.items():
            value = float(entry.get())
            if value > self.max_values[param]:
                messagebox.showerror("Error", f"{param} exceeds the maximum value of {self.max_values[param]}")
                return False
        return True
