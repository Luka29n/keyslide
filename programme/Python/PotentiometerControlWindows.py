import serial as serial
#import pyvolume
#import screen_brightness_control as sbc

# Set up serial communication with the Arduino
ser = serial.Serial('COM17', 9600)  # Replace COM3 with the actual serial port name

while True:
    # Read the percentage value from the Arduino
    data = ser.readline()
    if data:
        print(data)
        #percentage = int(data.decode().strip())
        #print(f"Received percentage: {percentage}%")

        # Map the percentage to a volume level (0-100)

        # Use pyautogui to simulate volume changes
        #pyvolume.custom(percent=percentage)  # Increase volume
        #sbc.set_brightness(percentage)

        #print(f"Volume set to: {percentage}%")