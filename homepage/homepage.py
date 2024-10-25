# homepage/homepage.py
import tkinter as tk
from homepage.submodules.connection.connection import ConnectionStatus
from homepage.submodules.mode_selection import ModeSelection
from homepage.submodules.user_actions import UserActions
from homepage.submodules.logout.logout import Logout
from homepage.submodules.ecg_test import ECGGraph

class Homepage:
    def __init__(self, username, show_login_page_callback):
        self.username = username
        self.show_login_page_callback = show_login_page_callback
        self.frame = None

    def show(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.connection_status = ConnectionStatus(self.frame)
        self.mode_selection = ModeSelection(self.frame, self.username)
        self.user_actions = UserActions(self.frame, self.username, self.mode_selection.variable, self.mode_selection.entries)
        self.logout = Logout(self.frame, root, self.show_login_page_callback)
        self.ecg_graph = ECGGraph()

        self.create_ecg_button()

    def create_ecg_button(self):
        ecg_button = tk.Button(self.frame, text="Show Graph", command=self.ecg_graph.display)
        ecg_button.pack()