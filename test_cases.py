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
    """Test cases for user authentication and registration."""

    def setUp(self):
        """Setup: Save a user to test login and registration logic."""
        self.users = {"admin": "password123"}
        save_users(self.users)

    def test_valid_login(self):
        """Test a valid login with correct credentials."""
        print("Running test_valid_login...")
        result = authenticate_user("admin", "password123")
        self.assertTrue(result, "Expected to authenticate 'admin' with the correct password.")
        print("Passed: Valid login test.")

    def test_invalid_login(self):
        """Test an invalid login with incorrect password."""
        print("Running test_invalid_login...")
        result = authenticate_user("admin", "wrongpassword")
        self.assertFalse(result, "Expected authentication to fail for incorrect password.")
        print("Passed: Invalid login test.")

    def test_register_user(self):
        """Test registering a new user successfully."""
        print("Running test_register_user...")
        success, message = register_user("new_user", "new_password")
        self.assertTrue(success, "Registration of new user should be successful.")
        self.assertEqual(message, "User registered successfully",
                         "Expected success message for user registration.")
        print("Passed: User registration test.")

    def test_register_existing_user(self):
        """Test registering a user with an existing username."""
        print("Running test_register_existing_user...")
        success, message = register_user("admin", "password123")
        self.assertFalse(success, "Registration should fail for existing username.")
        self.assertEqual(message, "Username already exists",
                         "Expected message for duplicate username registration.")
        print("Passed: Existing user registration test.")

# ParameterManager Tests
class TestParameterManager(unittest.TestCase):
    """Test cases for ParameterManager component."""

    def setUp(self):
        """Setup: Initialize Tkinter root and ParameterManager."""
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.manager = ParameterManager(self.frame)

    def test_get_parameters(self):
        """Test if the default parameters are correctly retrieved."""
        print("Running test_get_parameters...")
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
        actual = self.manager.get_parameters()
        self.assertEqual(actual, expected,
                         "Default parameters should match expected values.")
        print(f"Passed: Default parameters match expected values: {actual}")

    def test_validate_parameters_success(self):
        """Test parameter validation with valid values."""
        print("Running test_validate_parameters_success...")
        valid_params = {"Lower Rate Limit": 30, "Upper Rate Limit": 120}
        self.manager.set_parameters(valid_params)
        self.assertTrue(self.manager.validate_parameters(),
                        "Valid parameters should pass validation.")
        print("Passed: Valid parameters successfully validated.")

    def test_validate_parameters_failure(self):
        """Test parameter validation with values exceeding limits."""
        print("Running test_validate_parameters_failure...")
        invalid_params = {"Lower Rate Limit": 60, "Upper Rate Limit": 250}
        self.manager.set_parameters(invalid_params)
        self.assertFalse(self.manager.validate_parameters(),
                         "Parameters exceeding limits should fail validation.")
        print("Passed: Invalid parameters correctly failed validation.")

    def tearDown(self):
        """Teardown: Destroy Tkinter root."""
        self.root.destroy()

# UserActions Tests
class TestUserActions(unittest.TestCase):
    """Test cases for UserActions component."""

    def setUp(self):
        """Setup: Initialize UserActions with necessary components."""
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
        """Test successful parameter saving."""
        print("Running test_save_parameters_success...")
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

        self.assertDictEqual(saved_params, valid_params,
                             "Saved parameters should match the input values.")
        print("Passed: Parameters successfully saved.")

    def test_save_invalid_parameters(self):
        """Test saving parameters that fail validation."""
        print("Running test_save_invalid_parameters...")
        invalid_params = {"Lower Rate Limit": 60, "Upper Rate Limit": 250}
        self.parameter_manager.set_parameters(invalid_params)
        self.user_actions.save_parameters()
        user_dir = os.path.join("user_data", self.username)
        filepath = os.path.join(user_dir, "AOO_parameters.json")
        self.assertFalse(os.path.exists(filepath),
                         "Invalid parameters should not be saved.")
        print("Passed: Invalid parameters not saved.")

    def tearDown(self):
        """Teardown: Clean up user data and destroy Tkinter root."""
        user_dir = os.path.join("user_data", self.username)
        if os.path.exists(user_dir):
            for file in os.listdir(user_dir):
                os.remove(os.path.join(user_dir, file))
            os.rmdir(user_dir)
        self.root.destroy()


# ModeSelection Tests
class TestModeSelection(unittest.TestCase):
    """Test cases for mode selection functionality."""

    def setUp(self):
        """Setup: Initialize Tkinter root and ModeSelection."""
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.username = "test_user"
        self.mode_selection = ModeSelection(self.frame, self.username)

    def test_save_and_load_user_parameters(self):
        """Test saving and loading parameters for a specific mode."""
        print("Running test_save_and_load_user_parameters...")
        params = {"Lower Rate Limit": 40, "Upper Rate Limit": 150}
        self.mode_selection.save_user_parameters("AOO", params)

        loaded_params = self.mode_selection.load_user_parameters("AOO")
        self.assertEqual(loaded_params, params,
                         "Loaded parameters should match saved values.")
        print("Passed: User parameters successfully saved and loaded.")

    def test_mode_change(self):
        """Test if changing mode updates the parameters."""
        print("Running test_mode_change...")
        self.mode_selection.variable.set("VOO")
        params = self.mode_selection.load_user_parameters("VOO") or self.mode_selection.default_params
        self.assertEqual(params["Lower Rate Limit"], 20,
                         "Lower Rate Limit should revert to default (20) when mode changes.")
        print("Passed: Mode change correctly updated parameters.")

    def tearDown(self):
        """Teardown: Clean up user data and destroy Tkinter root."""
        user_dir = os.path.join("user_data", self.username)
        if os.path.exists(user_dir):
            for file in os.listdir(user_dir):
                os.remove(os.path.join(user_dir, file))
            os.rmdir(user_dir)
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
