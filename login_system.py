import tkinter as tk
from tkinter import messagebox
import json

# Path to the user data file
user_data_file = "users.json"

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

# Function to register a new user
def register_user():
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

# Function to login user
def login_user():
    username = entry_login_username.get()
    password = entry_login_password.get()
    
    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful. Welcome back, {}!".format(username))
        show_homepage()
    else:
        messagebox.showerror("Error", "Incorrect username or password.")

# Show homepage after successful login
def show_homepage():
    login_frame.pack_forget()  # Hide login frame
    homepage_frame.pack(fill="both", expand=True)

# Initialize the main window
root = tk.Tk()
root.title("User Login System")
root.geometry("500x400")

# Login and registration frame
login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)

# Homepage frame
homepage_frame = tk.Frame(root)
tk.Label(homepage_frame, text="Welcome to the Homepage!", font=('bold', 14)).pack(pady=20)

# Registration form in login frame
tk.Label(login_frame, text="Register", font=('bold', 14)).pack(pady=(10, 5))
entry_register_username = tk.Entry(login_frame)
entry_register_username.pack()
entry_register_password = tk.Entry(login_frame, show="*")
entry_register_password.pack()
tk.Button(login_frame, text="Register", command=register_user).pack(pady=10)

# Login form in login frame
tk.Label(login_frame, text="Login", font=('bold', 14)).pack(pady=(10, 5))
entry_login_username = tk.Entry(login_frame)
entry_login_username.pack()
entry_login_password = tk.Entry(login_frame, show="*")
entry_login_password.pack()
tk.Button(login_frame, text="Login", command=login_user).pack(pady=10)

root.mainloop()
