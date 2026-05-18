# Smart Light Control using Arduino + Bluetooth
# Python Version (MicroPython / Python Logic Representation)

# LED connected to pin 8

from machine import Pin
import time

# Initialize LED pin
led = Pin(8, Pin.OUT)

# Variable to store received data
data = ""

print("Smart Light System Started")

while True:

    # Read command from user/mobile app
    # Example: '1' for ON, '0' for OFF
    data = input("Enter Command (1 = ON, 0 = OFF): ")

    if data == '1':
        led.value(1)      # Turn LED ON
        print("LED ON")

    elif data == '0':
        led.value(0)      # Turn LED OFF
        print("LED OFF")

    else:
        print("Invalid Command")

    time.sleep(0.1)
