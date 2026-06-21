# если ESP32-S3

import machine
import neopixel
import asyncio

pin = machine.Pin(21, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

async def flicker_light(on:bool=False):
    
    if on:
        np[0] = (0, 40, 50)
        np.write()
        await asyncio.sleep(0.2)
    else:
        np[0] = (30, 40, 0)
        np.write()
        await asyncio.sleep(0.2)
        np[0] = (0, 0, 0)
        np.write()
        await asyncio.sleep(0.2)


#  Pico W

# import machine
# import neopixel
# import asyncio

# led = machine.Pin("LED", machine.Pin.OUT)

# pin = machine.Pin(21, machine.Pin.OUT)
# np = neopixel.NeoPixel(pin, 1)

# async def flicker_light(on: bool = False):
#     if on:
#         led.on()
#         await asyncio.sleep(0.2)
#     else:
#         led.on()
#         await asyncio.sleep(0.2)
#         led.off()
#         await asyncio.sleep(0.2)