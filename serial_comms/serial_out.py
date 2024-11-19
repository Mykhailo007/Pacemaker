import serial
import struct

def serial_out(packet, selected_mode):
  
  st = struct.Struct('<BBBBddBBddHHHBBBBBB')

  start_bit = bytes([0x16])
  fn_code = bytes([0x55])
  
  LRL = int(packet[0])
  URL = int(packet[1])
  MSR = int(packet[2])
  A_AMP = float(packet[3])
  A_PW = float(packet[4])
  V_AMP = float(packet[5])
  V_PW = float(packet[6])
  A_SENS = float(packet[7])
  V_SENS = float(packet[8])
  ARP = int(packet[9])
  VRP = int(packet[10])
  PVARP = int(packet[11])
  PVARP_EXT = int(packet[12])
  HYST = int(packet[13])
  RATE_SMOOTH = int(packet[14])
  ATR_DUR = int(packet[15])
  ATR_FALLmode = int(packet[16])
  ATR_FALLtime = int(packet[17])
  
  activity_threshold = {
    "v-low": 0,
    "low": 1,
    "med-low": 2,
    "med": 3,
    "med-high": 4,
    "high": 5,
    "v-high": 6
  }
  
  ACTTHRESH = activity_threshold(packet[18])
  REACT_TIME = int(packet[19])
  RESP_FACTOR = int(packet[20])
  REC_TIME = float(packet[21])
  
  port = 'COM6'
  
  uC = None
  
  try:
    uC = serial.Serial(port, baudrate=115200, timeout=1)
    
    serial_data = st.pack(
      start_bit, fn_code, int(selected_mode), LRL, URL, MSR, A_AMP, A_PW, V_AMP, V_PW, A_SENS, V_SENS, ARP, VRP, PVARP, PVARP_EXT, HYST, RATE_SMOOTH, ATR_DUR, ATR_FALLmode, ATR_FALLtime, ACTTHRESH, REACT_TIME, RESP_FACTOR, REC_TIME
    )
    
    print("Packet sent:", ' '.join(f"{x:02x}" for x in serial_data))
    print("Packet length:", len(serial_data))
    
    uC.write(serial_data)
    
    response = st.unpack(serial_data)
    print("Response received:", ' '.join(f"{x:02x}" for x in response))
    
  except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
  finally:
    if uC is not None:
      uC.close()