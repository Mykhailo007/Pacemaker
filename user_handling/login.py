import os
import tkinter as tk
from tkinter import messagebox
import json
from homepage.homepage import show_homepage

# Get the directory where this script is located
script_dir = os.path.dirname(__file__)

# Path to the user data file inside the 'user_handling' folder
user_data_file = os.path.join(script_dir, "users.json")

# Load existing users from file
def load_users():
    try:
        with open(user_data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save users to file
def save_users(users):
    with open(user_data_file, 'w') as file:
        json.dump(users, file, indent=4)

# Initialize users from file
users = load_users()

# Function to validate login
def login_user(entry_login_username, entry_login_password, login_window, start_login):
    username = entry_login_username.get()
    password = entry_login_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        login_window.destroy()  # Close the login window
        show_homepage()  # Open homepage
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Function to register a new user
def register_user(entry_register_username, entry_register_password):
    username = entry_register_username.get()
    password = entry_register_password.get()

    if len(users) >= 10:
        messagebox.showerror("Error", "Maximum user limit reached.")
        return
    
    if username in users:
        messagebox.showerror("Error", "User already exists.")
    else:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Success", "User registered successfully.")
