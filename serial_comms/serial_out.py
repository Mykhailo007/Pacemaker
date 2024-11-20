import serial
import struct

def serial_out(packet, selected_mode):
    
    # Format string for parameters:
    # H: uint16 (2 bytes)
    # d: double (8 bytes)
    st = struct.Struct('<HHHH8d8dHHHHHdHHHB')

    start_bit = bytes([0x16])
    fn_code = bytes([0x55])
    
    # Parameters matching MATLAB rxdata structure
    #Current_Mode = int(packet[0])       # uint16
    LRL = int(packet[0])                # uint16
    URL = int(packet[1])                # uint16
    Max_Sensor_Rate = int(packet[2])    # uint16
    A_Amplitude = float(packet[3])   # double
    V_Amplitude = float(packet[4])  # double
    A_Pulse_Width = int(packet[5])     # uint16
    V_Pulse_Width = int(packet[6])     # uint16
    A_Sensitivity = float(packet[7]) # double
    V_Sensitivity = float(packet[8]) # double
    VRP = int(packet[9])            # uint16
    ARP = int(packet[10])            # uint16
    PVARP = int(packet[11])          # uint16
    Hysteresis = int(packet[12])        # uint16
    Rate_Smoothing = int(packet[13])    # uint16
    activity_threshold_map = {
        "V-Low": 0,
        "Low": 1,
        "Med-Low": 2,
        "Med": 3,
        "Med-High": 4,
        "High": 5,
        "V-High": 6
    }
    
    Activity_Threshold = activity_threshold_map[data[14]]
    Reaction_Time = int(packet[15])     # uint16
    Response_Factor = int(packet[16])    # uint16
    Recovery_Time = int(packet[17])      # uint16
    #Green_Led = 1                       # uint8
    
    port = 'COM6'
    
    uC = None
    
    try:
      uC = serial.Serial(port, baudrate=115200)
    # Pack data according to struct format
      data = st.pack(
          int(selected_mode), LRL, URL, Max_Sensor_Rate,
          A_Amplitude, V_Amplitude,
          A_Pulse_Width, V_Pulse_Width,
          A_Sensitivity, V_Sensitivity,
          VRP, ARP, PVARP,
          Hysteresis, Rate_Smoothing,
          Activity_Threshold,
          Reaction_Time, Response_Factor, Recovery_Time,
          # Green_Led
      )
      
      print(data)
      print(len(data))
      
      uC.write(start_bit + fn_code + data)
      
      # Unpack data for debugging
      unpacked = st.unpack(data)
      print(unpacked)
      
    except serial.SerialException as e:
      print(f"Error: {e}")
      
    finally:
      if uC and uC.is_open:
        uC.close()
    