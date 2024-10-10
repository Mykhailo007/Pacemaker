import tkinter as tk
from login import login_user, register_user

# Function to start the login window
def start_login():
    global entry_login_username, entry_login_password, entry_register_username, entry_register_password

    login_window = tk.Tk()
    login_window.title("Login System")

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

    login_window.mainloop()

# Start the login process
start_login()
