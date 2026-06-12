import work_network 
from web import run_web
from light import flicker_light
import lora_work
import asyncio


nk = work_network
nk.run_network(essid='13', password='87654321')


async def connect_wifi():
    while True:
        await flicker_light(nk.get_isconnected())
        print(nk.get_isconnected())
        await asyncio.sleep(0.5)

async def main():
    asyncio.create_task(connect_wifi())
    asyncio.create_task(lora_work.lora_listen_mes())
    print('Запускаем сервер...')
    await run_web()


asyncio.run(main())