import serial
import struct

# Serial configuration parameters
frdm_port = "COM8"
baud_rate = 115200
timeout = 5

# Packet headers
Start = b'\x16'
SYNC = b'\x22'
Fn_set = b'\x55'

# Helper function to create a connection
def create_connection(port):
    try:
        return serial.Serial(port, baud_rate, timeout=timeout)
    except serial.SerialException:
        print("Failed to connect to the pacemaker.")
        return None

# Function to check connection by sending an echo signal
def check_connect():
    echo_signal = Start + SYNC + struct.pack("B", 2) + (b'\x00' * 71)
    with create_connection(frdm_port) as pacemaker:
        if pacemaker:
            pacemaker.write(echo_signal)
            # Implement read or response check if needed
            return True
    return False

# Function to send configuration to the pacemaker
def send_configuration(mode, lrl, url, settings):
    # Unpack settings tuple to individual parameters
    AA, APW, AST, VA, VPW, VST, sVRP, sARP, sPVARP, sRS, sMSR, reactionTime, responseFactor, recoveryTime, activityThreshold, HRL = settings
    
    signal_set_order = (Start + Fn_set + struct.pack("B", mode) + struct.pack("B", lrl) + struct.pack("B", url) +
                        struct.pack("H", sPVARP) + struct.pack("B", sRS) + struct.pack("H", reactionTime) +
                        struct.pack("B", responseFactor) + struct.pack("d", activityThreshold) + 
                        struct.pack("H", recoveryTime) + struct.pack("B", sMSR) + struct.pack("d", AA) +
                        struct.pack("d", APW) + struct.pack("H", sARP) + struct.pack("d", AST) +
                        struct.pack("d", VA) + struct.pack("d", VPW) + struct.pack("H", sVRP) +
                        struct.pack("d", VST))
    
    with create_connection(frdm_port) as pacemaker:
        if pacemaker:
            pacemaker.write(signal_set_order)
            # Additional commands can be added here if needed

# Function to read ECG data from the pacemaker
def read_ecg():
    request_signal = Start + SYNC + (b'\x00' * 72)
    with create_connection(frdm_port) as pacemaker:
        if pacemaker:
            pacemaker.write(request_signal)
            data = pacemaker.read(88)
            ATR_signal = struct.unpack("d", data[72:80])[0]
            VENT_signal = struct.unpack("d", data[80:88])[0]
            return ATR_signal, VENT_signal

# Example of sending data
settings = (3.5, 0.5, 1.2, 3.5, 0.5, 1.2, 250, 300, 150, 2, 160, 2000, 5, 2000, 1.5, 130)
send_configuration(1, 60, 120, settings)

# Example of reading ECG
atrial, ventricular = read_ecg()
print(f"Atrial Signal: {atrial}, Ventricular Signal: {ventricular}")
