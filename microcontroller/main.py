import work_network 
from web import run_web
from light import flicker_light
import lora_work
import asyncio
import sys


nk = work_network
nk.run_network(essid='esp32_s3_zero', password='87654321')


async def connect_wifi():
    while True:
        await flicker_light(nk.get_isconnected())
        print(nk.get_isconnected())
        await asyncio.sleep(0.5)

async def main():
    print('Запуск лоры...')
    try:
        asyncio.create_task(connect_wifi())
        asyncio.create_task(lora_work.lora_loop())
        print('Запускаем сервер...')
        await run_web()
    except Exception as e:
        print('ОШИБКА:', e)
        sys.print_exception(e)
        

asyncio.run(main())