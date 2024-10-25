# homepage/submodules/logout/logout.py
import tkinter as tk

class Logout:
    def __init__(self, frame, root, show_login_page_callback):
        self.frame = frame
        self.root = root
        self.show_login_page_callback = show_login_page_callback
        self.create_logout_button()

    def create_logout_button(self):
        logout_button = tk.Button(self.frame, text="Logout", command=self.logout)
        logout_button.pack()

    def logout(self):
        self.root.destroy()
        self.show_login_page_callback()

# login_page/login.py
import tkinter as tk
from tkinter import messagebox
from user_data.user_auth import register_user, authenticate_user

class LoginPage:
    def __init__(self, root, show_homepage_callback):
        self.root = root
        self.show_homepage_callback = show_homepage_callback
        self.root.title("Login")
        self.create_widgets()

    def create_widgets(self):
        self.create_login_section()
        self.create_register_section()
        self.create_close_button()

    def create_login_section(self):
        tk.Label(self.root, text="Username").grid(row=0, column=0, padx=10, pady=5)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Password").grid(row=1, column=0, padx=10, pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Login", command=self.login_user).grid(row=2, column=0, columnspan=2, pady=10)

    def create_register_section(self):
        tk.Label(self.root, text="Username").grid(row=3, column=0, padx=10, pady=5)
        self.entry_register_username = tk.Entry(self.root)
        self.entry_register_username.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Password").grid(row=4, column=0, padx=10, pady=5)
        self.entry_register_password = tk.Entry(self.root, show="*")
        self.entry_register_password.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Register", command=self.register_user_gui).grid(row=5, column=0, columnspan=2, pady=10)

    def create_close_button(self):
        tk.Button(self.root, text="Close", command=self.close_program).grid(row=6, column=0, columnspan=2, pady=10)

    def login_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if authenticate_user(username, password):
            self.root.destroy()
            self.show_homepage_callback(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register_user_gui(self):
        username = self.entry_register_username.get()
        password = self.entry_register_password.get()
        success, message = register_user(username, password)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def close_program(self):
        self.root.destroy()

def show_login_page(show_homepage_callback):
    root = tk.Tk()
    LoginPage(root, show_homepage_callback)
    root.mainloop()