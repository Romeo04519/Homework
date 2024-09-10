from time import sleep
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        print(f'Силач {name} поднял {i}')
        await asyncio.sleep(8//power)
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Heracl', 7))
    task2 = asyncio.create_task(start_strongman('Pluton', 1))
    task3 = asyncio.create_task(start_strongman('Apollon', 3))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())