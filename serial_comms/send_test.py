import serial
import struct
import time

# Serial port configuration
port_name = 'COM6'  # Change this to your COM port
baud_rate = 115200

# Packet structure
SYNC = 0x16
FN_CODE_SET = 0x55
FN_CODE_ECHO = 0x22
RED_ENABLE = 1
GREEN_ENABLE = 1
BLUE_ENABLE = 1
OFF_TIME = 1000  # example off time in milliseconds
SWITCH_TIME = 500  # example switch time in milliseconds

def create_packet(fn_code, red_enable, green_enable, blue_enable, off_time, switch_time):
    """Pack data into the specified format."""
    packet = struct.pack('<BBBBIH', SYNC, fn_code, red_enable, green_enable, blue_enable, off_time, switch_time)
    return packet

def send_packet(packet):
    """Send a packet over the serial port and read the response."""
    try:
        ser = serial.Serial(port_name, baud_rate, timeout=1)
        ser.write(packet)
        print("Packet sent:", ' '.join(f"{x:02x}" for x in packet))
        
        # Read response (loopback)
        time.sleep(1)  # Wait for the data to be looped back
        response = ser.read(len(packet))  # Read the same number of bytes as sent
        print("Response received:", ' '.join(f"{x:02x}" for x in response))
        
        ser.close()
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")

# Example usage
packet = create_packet(FN_CODE_SET, RED_ENABLE, GREEN_ENABLE, BLUE_ENABLE, OFF_TIME, SWITCH_TIME)
send_packet(packet)