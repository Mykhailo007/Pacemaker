import tkinter as tk
from tkinter import Toplevel
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from homepage.submodules.logout.logout import logout


def generate_ecg(length=1000):
    t = np.linspace(0, 1, length)
    heartbeat = np.sin(2 * np.pi * 5 * t) + np.random.normal(0, 0.1, length)
    qrs_peaks = np.sin(2 * np.pi * 30 * t)**2 * (np.random.normal(0.5, 0.15, length) > 0.65)
    return t, heartbeat + qrs_peaks * 1.5

def display_ecg_graph():
    # Create the main window
    ECG = tk.Tk()
    ECG.title("ECG Display")

    # Generate ECG data
    t, ecg_signal = generate_ecg()

    # Create a figure and a plot
    fig, ax = plt.subplots()
    ax.plot(t, ecg_signal, label='Heartbeat')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Amplitude')
    ax.set_title('ECG Graph')
    ax.legend()
    ax.grid(True)

    # Create a canvas and integrate it into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ECG)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    back_button = tk.Button(ECG, text="Close", command=lambda: ECG.destroy())
    back_button.pack()

    #logout_button = tk.Button(ECG, text="Logout", command=lambda: logout(ECG))
    #logout_button.pack()

    # Start the GUI event loop
    ECG.mainloop()

