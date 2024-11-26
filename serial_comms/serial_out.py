import serial
import struct
import time

class SerialOut:
    def __init__(self, port_name='COM3', baud_rate=115200):
        self.port_name = port_name
        self.baud_rate = baud_rate
        self.st = struct.Struct('<HHHH8d8dHHHHHdHHHB')
        self.start_bit = bytes([0x16])
        self.fn_code = bytes([0x55])

    def send_packet(self, packet, selected_mode):
        # Parameters matching MATLAB rxdata structure
        Current_Mode = int(packet[0])       # uint16
        LRL = int(packet[1])                # uint16
        URL = int(packet[2])                # uint16
        Max_Sensor_Rate = int(packet[3])    # uint16
        A_Amplitude = float(packet[4])   # double
        V_Amplitude = float(packet[5])  # double
        A_Pulse_Width = int(packet[6])     # uint16
        V_Pulse_Width = int(packet[7])     # uint16
        A_Sensitivity = float(packet[8]) # double
        V_Sensitivity = float(packet[9]) # double
        VRP = int(packet[10])            # uint16
        ARP = int(packet[11])            # uint16
        PVARP = int(packet[12])          # uint16
        Hysteresis = int(packet[13])        # uint16
        Rate_Smoothing = int(packet[14])    # uint16
        Activity_Threshold = float(packet[15]) # double
        Reaction_Time = int(packet[16])     # uint16
        Response_Factor = int(packet[17])    # uint16
        Recovery_Time = int(packet[18])      # uint16
        Green_Led = int(packet[19])          # uint8

        # Pack data according to struct format
        data = self.st.pack(
            Current_Mode, LRL, URL, Max_Sensor_Rate,
            A_Amplitude, V_Amplitude,
            A_Pulse_Width, V_Pulse_Width,
            A_Sensitivity, V_Sensitivity,
            VRP, ARP, PVARP,
            Hysteresis, Rate_Smoothing,
            Activity_Threshold,
            Reaction_Time, Response_Factor, Recovery_Time,
            Green_Led
        )

        packet = self.start_bit + self.fn_code + data

        try:
            ser = serial.Serial(self.port_name, self.baud_rate, timeout=1)
            ser.write(packet)
            print("Packet sent:", ' '.join(f"{x:02x}" for x in packet))
            
            # Read response (loopback)
            time.sleep(1)  # Wait for the data to be looped back
            response = ser.read(len(packet))  # Read the same number of bytes as sent
            print("Response received:", ' '.join(f"{x:02x}" for x in response))
            
            ser.close()
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")