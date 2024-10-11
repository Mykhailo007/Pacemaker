import tkinter as tk
from tkinter import messagebox, PhotoImage, Menu
import json
from PIL import Image, ImageTk

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
    label_register.config(text=current_language["register"])
    label_login.config(text=current_language["login"])
    button_register.config(text=current_language["submit"])
    button_login.config(text=current_language["submit"])
    entry_login_username.delete(0, tk.END)
    entry_login_password.delete(0, tk.END)

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

def load_language(lang='english'):
    with open(f"languages/{lang}.json", 'r', encoding='utf-8') as file:
        return json.load(file)
    
# Handle placeholder logic
def on_entry_click(event, default_text):
    """Function to be called when the entry is clicked."""
    current = event.widget.get()
    if current == default_text:
        event.widget.delete(0, tk.END)  # delete all the text in the entry
        event.widget.insert(0, '')  # Insert blank for user input
        event.widget.config(fg='black')

def on_focusout(event, default_text):
    """Function to be called when focus is moved away from the entry."""
    if event.widget.get() == '':
        event.widget.insert(0, default_text)
        event.widget.config(fg='grey')

def add_placeholder(entry_widget, placeholder_text):
    entry_widget.insert(0, placeholder_text)
    entry_widget.config(fg='grey')
    entry_widget.bind('<FocusIn>', lambda event, text=placeholder_text: on_entry_click(event, text))
    entry_widget.bind('<FocusOut>', lambda event, text=placeholder_text: on_focusout(event, text))



# Initialize the main window
root = tk.Tk()
root.title("Pacemaker")
root.geometry("500x500")
root.configure(bg='#f0f0f0')  # Light grey background for the window

# Menu for language selection
menu = Menu(root)
root.config(menu=menu)
language_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Language", menu=language_menu)
language_menu.add_command(label="English", command=lambda: set_language('english'))
language_menu.add_command(label="Dutch", command=lambda: set_language('dutch'))
language_menu.add_command(label="French", command=lambda: set_language('french'))
language_menu.add_command(label="Spanish", command=lambda: set_language('spanish'))
language_menu.add_command(label="Swedish", command=lambda: set_language('swedish'))

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
label_register = tk.Label(login_frame, text="Register", font=('Helvetica', 18), bg='#ffffff')
label_register.pack(pady=(10, 5))
entry_register_username = tk.Entry(login_frame, font=('Helvetica', 14), bd=1, relief="solid")
entry_register_username.pack()
entry_register_password = tk.Entry(login_frame, show="*", font=('Helvetica', 14), bd=1, relief="solid")
entry_register_password.pack()
button_register = tk.Button(login_frame, font=('Helvetica', 14), bg='#008CBA', fg='white', command=register_user)
button_register.pack(pady=10)

# Login form in login frame
label_login = tk.Label(login_frame, font=('Helvetica', 18), bg='#ffffff')
label_login.pack(pady=(10, 5))
entry_login_username = tk.Entry(login_frame, font=('Helvetica', 14), bd=1, relief="solid")
entry_login_username.pack()
entry_login_password = tk.Entry(login_frame, show="*", font=('Helvetica', 14), bd=1, relief="solid")
entry_login_password.pack()
button_login = tk.Button(login_frame, font=('Helvetica', 14), bg='#008CBA', fg='white', relief="groove", command=login_user)
button_login.pack(pady=10)

update_ui_texts()
root.mainloop()


