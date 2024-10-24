import tkinter as tk
from tkinter import Menu
import json
from user_handling.login import login_user, register_user

def load_language(lang='english'):
    with open(f"languages/{lang}.json", 'r', encoding='utf-8') as file:
        return json.load(file)
    
# Current language is set to English by default
current_language = load_language('english')

def set_language(lang):
    global current_language
    current_language = load_language(lang)
    update_ui_texts()
    
def update_ui_texts():
    global label_login, label_username, label_password, label_register, label_register_username, label_register_password, register_button, login_button
    label_login.config(text=current_language["login"])
    label_username.config(text=current_language["username"])
    label_password.config(text=current_language["password"])
    label_register.config(text=current_language["register"])
    label_register_username.config(text=current_language["username"])
    label_register_password.config(text=current_language["password"])
    register_button.config(text=current_language["register"])
    login_button.config(text=current_language["login"])
    entry_login_username.delete(0, tk.END)
    entry_login_password.delete(0, tk.END)

# Function to start the login window
def start_login():
    global entry_login_username, entry_login_password, entry_register_username, entry_register_password
    global label_login, label_username, label_password, label_register, label_register_username, label_register_password, register_button, login_button

    login_window = tk.Tk()
    login_window.title("Login System")
    login_window.state('zoomed')  # Maximize window

    # Menu for language selection
    menu = Menu(login_window)
    login_window.config(menu=menu)
    language_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Language", menu=language_menu)
    language_menu.add_command(label="English", command=lambda: set_language('english'))
    language_menu.add_command(label="Dutch", command=lambda: set_language('dutch'))
    language_menu.add_command(label="Danish", command=lambda: set_language('danish'))
    language_menu.add_command(label="French", command=lambda: set_language('french'))
    language_menu.add_command(label="German", command=lambda: set_language('german'))
    language_menu.add_command(label="Italian", command=lambda: set_language('italian'))
    language_menu.add_command(label="Spanish", command=lambda: set_language('spanish'))
    language_menu.add_command(label="Swedish", command=lambda: set_language('swedish'))

    # Login section
    label_login = tk.Label(login_window, text="Login", font=("Arial", 14))
    label_login.grid(row=0, column=0, padx=10, pady=10)

    label_username = tk.Label(login_window, text="Username")
    label_username.grid(row=1, column=0, padx=10, pady=5)
    entry_login_username = tk.Entry(login_window)
    entry_login_username.grid(row=1, column=1, padx=10, pady=5)

    label_password = tk.Label(login_window, text="Password")
    label_password.grid(row=2, column=0, padx=10, pady=5)
    entry_login_password = tk.Entry(login_window, show="*")
    entry_login_password.grid(row=2, column=1, padx=10, pady=5)

    login_button = tk.Button(login_window, text="Login", command=lambda: login_user(entry_login_username, entry_login_password, login_window, start_login))
    login_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Registration section
    label_register = tk.Label(login_window, text="Register", font=("Arial", 14))
    label_register.grid(row=4, column=0, padx=10, pady=10)

    label_register_username = tk.Label(login_window, text="Username")
    label_register_username.grid(row=5, column=0, padx=10, pady=5)
    entry_register_username = tk.Entry(login_window)
    entry_register_username.grid(row=5, column=1, padx=10, pady=5)

    label_register_password = tk.Label(login_window, text="Password")
    label_register_password.grid(row=6, column=0, padx=10, pady=5)
    entry_register_password = tk.Entry(login_window, show="*")
    entry_register_password.grid(row=6, column=1, padx=10, pady=5)

    register_button = tk.Button(login_window, text="Register", command=lambda: register_user(entry_register_username, entry_register_password))
    register_button.grid(row=7, column=0, columnspan=2, pady=10)

    update_ui_texts()
    login_window.mainloop()

# Start the login process
start_login()
