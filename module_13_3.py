from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text= ['Привет', 'привет', 'добрый день'])
async def greet(message):
    print("Вам письмо!")
    await message.answer('Введите команду /start, чтобы начать общение')

@dp.message_handler(commands=['start'])
async def start(message):
    print("Гость начал беседу")
    await message.answer('Привет, я бот помогающий твоему здоровью!')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
