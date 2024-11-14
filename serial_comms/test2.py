import serial
import struct

def create_packet(red_enable, green_enable, blue_enable, off_time, switch_time):
    sync_byte = 0x16  # Constant for SYNC
    fn_code = 0x55    # Constant for setting parameters (use 0x22 for echo)
    
    # Packing data according to the specified format
    packet = struct.pack('BBB', sync_byte, fn_code, red_enable)
    packet += struct.pack('B', green_enable)
    packet += struct.pack('B', blue_enable)
    packet += struct.pack('f', off_time)
    packet += struct.pack('H', switch_time)
    
    return packet

def print_packet(packet):
    print('Packet Hex:', ' '.join(f"{byte:02x}" for byte in packet))

    # Ensure the packet has the correct length
    if len(packet) != 11:
        print(f"Error: Incorrect packet size {len(packet)}; expected 11 bytes.")
        return
    
    # Unpack and print the packet details
    try:
        sync, fn_code, red, green, blue, off_time, switch_time = struct.unpack('<BBBBBfH', packet)
        print(f"SYNC: {sync}, FN_CODE: {fn_code}, RED_ENABLE: {red}, GREEN_ENABLE: {green}, BLUE_ENABLE: {blue}, OFF_TIME: {off_time}, SWITCH_TIME: {switch_time}")
    except struct.error as e:
        print(f"Failed to unpack packet: {e}")

# Setup serial connection
ser = serial.Serial(
    port='COM6', # Replace 'COM_PORT' with your actual serial port
    baudrate=115200,
    timeout=1
)

# Example data to send
red_enable = 1   # Enable RED
green_enable = 1 # Enable GREEN
blue_enable = 1  # Enable BLUE
off_time = 1.0   # 1 second OFF time
switch_time = 500 # 500 milliseconds SWITCH time

# Create the packet
packet = create_packet(red_enable, green_enable, blue_enable, off_time, switch_time)

# Print the packet before sending
print_packet(packet)

# Send the packet
ser.write(packet)

# Close the connection
ser.close()
