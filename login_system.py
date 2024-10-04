import tkinter as tk
from tkinter import messagebox, PhotoImage
import json
from PIL import Image, ImageTk

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
root.title("Pacemaker")
root.geometry("500x500")
root.configure(bg='#f0f0f0')  # Light grey background for the window

# Load an image
image_path = "logo.png"  # Make sure the path to your logo image is correct
logo = Image.open(image_path)
logo = logo.resize((100, 100), Image.Resampling.LANCZOS)  # Resize the logo to 100x100 pixels
logo_image = ImageTk.PhotoImage(logo)

# Login and registration frame
login_frame = tk.Frame(root, bg='#ffffff')
login_frame.pack(pady=20)

# Displaying the logo at the top of the login frame
logo_label = tk.Label(login_frame, image=logo_image, bg='#ffffff')
logo_label.pack(pady=10)

# Homepage frame
homepage_frame = tk.Frame(root)
tk.Label(homepage_frame, text="Welcome to Diddy's After Party!", font=('bold', 16)).pack(pady=20)

# Registration form in login frame
tk.Label(login_frame, text="Register", font=('Helvetica', 18), bg='#ffffff').pack(pady=(10, 5))
entry_register_username = tk.Entry(login_frame, font=('Helvetica', 12), bd=1, relief="solid")
entry_register_username.pack()
entry_register_password = tk.Entry(login_frame, font=('Helvetica', 12), show="*", bd=1, relief="solid")
entry_register_password.pack()
tk.Button(login_frame, text="Register", command=register_user).pack(pady=10)

# Login form in login frame
tk.Label(login_frame, text="Login", font=('Helvetica', 14), bg='#ffffff').pack(pady=(10, 5))
entry_login_username = tk.Entry(login_frame, font=('Helvetica', 12), bd=1, relief="solid")
entry_login_username.pack()
entry_login_password = tk.Entry(login_frame, show="*", font=('Helvetica', 12), bd=1, relief="solid")
entry_login_password.pack()
tk.Button(login_frame, text="Login", font=('Helvetica', 12), bg='#008CBA', fg='white', relief="groove", command=login_user).pack(pady=10)

root.mainloop()


