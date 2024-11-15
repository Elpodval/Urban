import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in range(1, 6):
        # Задержка обратно пропорциональна силе (чем больше сила, тем меньше задержка)
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Создаем задачи для трех силачей с разными именами и силой
    strongman1 = asyncio.create_task(start_strongman("Иван", 5))
    strongman2 = asyncio.create_task(start_strongman("Алексей", 3))
    strongman3 = asyncio.create_task(start_strongman("Сергей", 4))

    # Ожидаем завершения всех задач
    await strongman1
    await strongman2
    await strongman3


# Запускаем асинхронную функцию start_tournament
asyncio.run(start_tournament())