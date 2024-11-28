import tkinter as tk
from tkinter import messagebox

class Parameters:
    def __init__(self, frame):
        self.frame = frame
        self.params = {
            "Lower Rate Limit": 60, 
            "Upper Rate Limit": 120, 
            "Maximum Sensor Rate": 120,
            "Atrial Amplitude": 5.0, 
            "Atrial Pulse Width": 1, 
            "Ventricular Amplitude": 5.0, 
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
        self.entries = self.create_parameters()

    def create_parameters(self):
        entries = {}
        for param, value in self.params.items():
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
