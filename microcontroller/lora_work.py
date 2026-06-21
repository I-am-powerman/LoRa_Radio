from machine import SPI, Pin
from lib.ulora.core import ULoRa
import state
import asyncio

# Пины для ESP32-S3 Zero
spi = SPI(1, baudrate=5_000_000, polarity=0, phase=0,
          sck=Pin(12), mosi=Pin(11), miso=Pin(13))
          
pins = {
    "ss": 10, 
    "reset": 8, 
    "dio0": 9 
}

# Пины для raspberry pi pico w нужны номера GPIO
# spi = SPI(0, baudrate=5_000_000, polarity=0, phase=0,
#           sck=Pin(18), mosi=Pin(19), miso=Pin(16))
          
# pins = {
#     "ss": 17, 
#     "reset": 21, 
#     "dio0": 20 
# }

lora = ULoRa(spi, pins)

outbox = []  # сообщения ожидающие отправки

async def lora_loop():
    while True:
        if state.is_listening:
            # 1. Отправляем если есть что
            if outbox:
                msg = outbox.pop(0)
                lora.println(msg, repeat=2) # repeat подстраховка на случай потери
                print('Отправлено:', msg)


            # 2. Слушаем
            raw = lora.listen() # работает без timeout
            if raw:
                state.messages.append({
                    'text': raw,
                    'sender': 'friend',
                    'time': '--:--'
                })
            print(raw)


        await asyncio.sleep(0)