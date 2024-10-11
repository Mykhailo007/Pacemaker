import os
import json

def load_user_data(username):
    # Path to user-specific data
    user_data_path = os.path.join('user_handling', f'{username}_data.json')
    
    # If the user data doesn't exist, create it
    if not os.path.exists(user_data_path):
        # Initialize an empty data structure with default values for each mode
        user_data = {
            "aoo": {
                "lower_rate_limit": 60,
                "upper_rate_limit": 120,
                "atrial_amplitude": 3.5,
                "atrial_pulse_width": 0.4
            },
            "voo": {
                "lower_rate_limit": 65,
                "upper_rate_limit": 115,
                "ventricular_amplitude": 4.0,
                "ventricular_pulse_width": 0.5
            },
            "aai": {
                "lower_rate_limit": 70,
                "upper_rate_limit": 130,
                "atrial_amplitude": 2.5,
                "atrial_pulse_width": 0.3
            },
            "vvi": {
                "lower_rate_limit": 60,
                "upper_rate_limit": 110,
                "ventricular_amplitude": 3.0,
                "ventricular_pulse_width": 0.4
            }
        }
        with open(user_data_path, 'w') as file:
            json.dump(user_data, file, indent=4)
    else:
        with open(user_data_path, 'r') as file:
            user_data = json.load(file)
    
    return user_data

def save_user_data(username, mode, updated_values):
    user_data_path = os.path.join('user_handling', f'{username}_data.json')
    
    with open(user_data_path, 'r') as file:
        user_data = json.load(file)
    
    # Update the specific mode values
    user_data[mode] = updated_values
    
    # Save back to file
    with open(user_data_path, 'w') as file:
        json.dump(user_data, file, indent=4)
