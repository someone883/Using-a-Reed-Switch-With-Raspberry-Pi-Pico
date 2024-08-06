#importing libraries
import machine
import utime
#making variables
reed = machine.Pin(14, machine.Pin.IN)
while True:
    if reed.value() == 1:
        print("ON")
        utime.sleep(1)
    else:
        print("OFF")
        utime.sleep(1)