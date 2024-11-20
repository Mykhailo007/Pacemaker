# navigation/page_navigator.py
from login_page.login import LoginPage
from homepage.homepage import Homepage
import tkinter as tk

class PageNavigator:
    def __init__(self):
        self.username = None

    def start(self):
        self.show_login_page()

    def show_login_page(self):
        root = tk.Tk()
        LoginPage(root, self.show_homepage)
        root.mainloop()

    def show_homepage(self, username):
        self.username = username
        root = tk.Tk()
        homepage = Homepage(self.username, self.show_login_page)
        homepage.show(root)    
            
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
