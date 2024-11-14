import serial
import time

# Configuration parameters
serial_port = 'COM8'  # Adjust this to the correct COM port
baud_rate = 115200  # Set to your microcontroller's configured baud rate

# Create the serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

def toggle_led():
    try:
        while True:
            # Send the 'ON' command to the microcontroller
            ser.write(b'ON\n')
            print("LED ON")
            time.sleep(1)  # Wait for 1 second

            # Send the 'OFF' command to the microcontroller
            ser.write(b'OFF\n')
            print("LED OFF")
            time.sleep(1)  # Wait for 1 second

    except KeyboardInterrupt:
        print("Program interrupted by the user.")

    finally:
        ser.close()  # Ensure the serial connection is closed on program exit

# Run the toggle function
if __name__ == '__main__':
    toggle_led()
