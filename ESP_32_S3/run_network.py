import network
import machine
import neopixel
import time

ap = network.WLAN(network.AP_IF)
pin = machine.Pin(21, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

ap.config(
    essid = 'Lerka_small_berserk',
    password = '87654321',
    authmode = network.AUTH_WPA2_PSK 
)

ap.active(True)

print(ap.status())
print(ap.ifconfig())

while True:
    if ap.isconnected():
        np[0] = (0, 40, 50)
        np.write()
        time.sleep(0.5)
    else:
        np[0] = (30, 40, 0)
        np.write()
        time.sleep(0.5)
        np[0] = (0, 0, 0)
        np.write()
        time.sleep(0.5)

# ap.active(False)
