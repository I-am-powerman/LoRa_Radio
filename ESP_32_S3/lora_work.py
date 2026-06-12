from machine import SPI, Pin
from lib.ulora.core import ULoRa
from state import messages
import asyncio

spi = SPI(1, baudrate=5_000_000, polarity=0, phase=0,
          sck=Pin(12), mosi=Pin(11), miso=Pin(13))
          
pins = {
    "ss": 10, 
    "reset": 14, 
    "dio0": 15 
}

lora = ULoRa(spi, pins, freq=433E6)

async def lora_send_mes(message):
    lora.println(message)
    print('Отправлено: ', message)
    await asyncio.sleep(0.1)

async def lora_listen_mes():
    while True:
        if lora.check():
            raw = lora.listen(timeout=500)
            if raw:
                messages.append({
                    'text': raw,
                    'sender': 'friend',
                    'time': '--:--'
                })
            print('Получено:', raw)
        await asyncio.sleep(0.1)