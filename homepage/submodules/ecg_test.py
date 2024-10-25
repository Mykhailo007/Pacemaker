# homepage/submodules/ecg_test.py
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ECGGraph:
    def __init__(self, length=1000):
        self.length = length
        self.t, self.ecg_signal = self.generate_ecg()

    def generate_ecg(self):
        t = np.linspace(0, 1, self.length)
        heartbeat = np.sin(2 * np.pi * 5 * t) + np.random.normal(0, 0.1, self.length)
        qrs_peaks = np.sin(2 * np.pi * 30 * t)**2 * (np.random.normal(0.5, 0.15, self.length) > 0.65)
        return t, heartbeat + qrs_peaks * 1.5

    def display(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("ECG Display")

        # Create a figure and a plot
        fig, ax = plt.subplots()
        ax.plot(self.t, self.ecg_signal, label='Heartbeat')
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Amplitude')
        ax.set_title('ECG Graph')
        ax.legend()
        ax.grid(True)

        # Create a canvas and integrate it into Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        back_button = tk.Button(self.root, text="Close", command=self.root.destroy)
        back_button.pack()

        # Start the GUI event loop
        self.root.mainloop()
