import asyncio

# Асинхронная функция для работы каждого силача
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):  # Поднимаем 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

# Асинхронная функция для проведения турнира
async def start_tournament():
    # Создаем три задачи с разными участниками
    tasks = [
        asyncio.create_task(start_strongman("Pasha", 3)),
        asyncio.create_task(start_strongman("Denis", 4)),
        asyncio.create_task(start_strongman("Apollon", 5))
    ]
    # Ожидаем выполнения всех задач
    await asyncio.gather(*tasks)

# Запуск программы
if __name__ == "__main__":
    asyncio.run(start_tournament())