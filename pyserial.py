import serial

s = serial.Serial('COM3', 115200, timeout = 10)
                            
print("Opening: " + s.name)

while True:
    # reset the buffers of the UART port to delete the remaining data in the buffers
    s.reset_output_buffer()
    s.reset_input_buffer()
        r = s.readline()

    
            r = s.readline()                    
            
                print("Stopping Transmission... Erasing Data... Return to Start")
                stop = 1
                break

    print("Close the serial port with s.close()")
