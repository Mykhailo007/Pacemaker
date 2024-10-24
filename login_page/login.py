# login_page/login.py
import tkinter as tk
from tkinter import messagebox
from homepage.homepage import show_homepage
from user_data.user_auth import register_user, authenticate_user

def show_login_page():
    global login_window
    login_window = tk.Tk()
    login_window.title("Login")

    label_username = tk.Label(login_window, text="Username")
    label_username.grid(row=0, column=0, padx=10, pady=5)
    entry_username = tk.Entry(login_window)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    label_password = tk.Label(login_window, text="Password")
    label_password.grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(login_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    login_button = tk.Button(login_window, text="Login", command=lambda: login_user(entry_username, entry_password))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    label_register_username = tk.Label(login_window, text="Username")
    label_register_username.grid(row=3, column=0, padx=10, pady=5)
    entry_register_username = tk.Entry(login_window)
    entry_register_username.grid(row=3, column=1, padx=10, pady=5)

    label_register_password = tk.Label(login_window, text="Password")
    label_register_password.grid(row=4, column=0, padx=10, pady=5)
    entry_register_password = tk.Entry(login_window, show="*")
    entry_register_password.grid(row=4, column=1, padx=10, pady=5)

    register_button = tk.Button(login_window, text="Register", command=lambda: register_user_gui(entry_register_username, entry_register_password))
    register_button.grid(row=5, column=0, columnspan=2, pady=10)

    login_window.mainloop()

def register_user_gui(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    success, message = register_user(username, password)
    if success:
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Error", message)

def login_user(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if authenticate_user(username, password):
        login_window.destroy()
        show_homepage(username)
    else:
        messagebox.showerror("Error", "Invalid username or password")