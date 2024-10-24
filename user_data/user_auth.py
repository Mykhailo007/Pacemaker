# user_handling/user_auth.py
import json
import os

USER_DATA_FILE = "user_data/users.json"

def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists"
    users[username] = password
    save_users(users)
    return True, "User registered successfully"

def authenticate_user(username, password):
    users = load_users()
    if username in users and users[username] == password:
        return True
    return False