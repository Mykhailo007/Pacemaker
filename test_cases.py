import unittest
import os
import json
import tkinter as tk
from homepage.submodules.parameters import ParameterManager
from homepage.submodules.user_actions import UserActions
from homepage.submodules.mode_selection import ModeSelection
from user_data.user_auth import authenticate_user, register_user, load_users, save_users

# Authentication Tests
class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.users = {"admin": "password123"}
        save_users(self.users)

    def test_valid_login(self):
        self.assertTrue(authenticate_user("admin", "password123"))

    def test_invalid_login(self):
        self.assertFalse(authenticate_user("admin", "wrongpassword"))

    def test_register_user(self):
        success, message = register_user("new_user", "new_password")
        self.assertTrue(success)
        self.assertEqual(message, "User registered successfully")

    def test_register_existing_user(self):
        success, message = register_user("admin", "password123")
        self.assertFalse(success)
        self.assertEqual(message, "Username already exists")

# ParameterManager Tests
class TestParameterManager(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.manager = ParameterManager(self.frame)

    def test_get_parameters(self):
        expected = {
            "Lower Rate Limit": 20.0,
            "Upper Rate Limit": 100.0,
            "Atrial Amplitude": 2.5,
            "Atrial Pulse Width": 0.4,
            "Ventricular Amplitude": 3.0,
            "Ventricular Pulse Width": 0.6,
            "Atrial Refactory Period": 10.0,
            "Ventricular Refactory Period": 15.0
        }
        self.assertEqual(self.manager.get_parameters(), expected)

    def test_validate_parameters_success(self):
        valid_params = {"Lower Rate Limit": 30, "Upper Rate Limit": 120}
        self.manager.set_parameters(valid_params)
        self.assertTrue(self.manager.validate_parameters())

    def test_validate_parameters_failure(self):
        invalid_params = {"Lower Rate Limit": 60, "Upper Rate Limit": 250}
        self.manager.set_parameters(invalid_params)
        self.assertFalse(self.manager.validate_parameters())

    def tearDown(self):
        self.root.destroy()

# UserActions Tests
class TestUserActions(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.username = "test_user"
        self.parameter_manager = ParameterManager(self.frame)
        self.variable = tk.StringVar(self.frame)
        self.variable.set("AOO")

        self.user_actions = UserActions(
            self.frame, self.username, self.variable, self.parameter_manager
        )

    def test_save_parameters_success(self):
        valid_params = {
            "Lower Rate Limit": 30,
            "Upper Rate Limit": 120,
            "Atrial Amplitude": 2.5,
            "Atrial Pulse Width": 0.4,
            "Ventricular Amplitude": 3.0,
            "Ventricular Pulse Width": 0.6,
            "Atrial Refactory Period": 10.0,
            "Ventricular Refactory Period": 15.0
        }

        self.parameter_manager.set_parameters(valid_params)
        self.user_actions.save_parameters()

        user_dir = os.path.join("user_data", self.username)
        filepath = os.path.join(user_dir, "AOO_parameters.json")

        with open(filepath, 'r') as file:
            saved_params = json.load(file)

        self.assertDictEqual(saved_params, valid_params)

    def tearDown(self):
        user_dir = os.path.join("user_data", self.username)
        if os.path.exists(user_dir):
            for file in os.listdir(user_dir):
                os.remove(os.path.join(user_dir, file))
            os.rmdir(user_dir)
        self.root.destroy()

# ModeSelection Tests
class TestModeSelection(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.username = "test_user"
        self.mode_selection = ModeSelection(self.frame, self.username)

    def test_save_and_load_user_parameters(self):
        params = {"Lower Rate Limit": 40, "Upper Rate Limit": 150}
        self.mode_selection.save_user_parameters("AOO", params)

        loaded_params = self.mode_selection.load_user_parameters("AOO")
        self.assertEqual(loaded_params, params)

    def test_mode_change(self):
        self.mode_selection.variable.set("VOO")
        params = self.mode_selection.load_user_parameters("VOO") or self.mode_selection.default_params
        self.assertEqual(params["Lower Rate Limit"], 20, "Lower Rate Limit should be updated to 20.")

    def tearDown(self):
        user_dir = os.path.join("user_data", self.username)
        if os.path.exists(user_dir):
            for file in os.listdir(user_dir):
                os.remove(os.path.join(user_dir, file))
            os.rmdir(user_dir)
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
