from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import logging


api = "7450150397:AAH_pF5Zt4l36wyWY5WNbqkl9J1Zap2ZKKo"
bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация'))


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(text='Привет! Я бот, помогающий твоему здоровью!', reply_markup=kb)


@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # используем формулу для женщин
    calories = 10 * weight + 6.25 * growth - 5 * age + 161

    await message.answer(f"Ваша норма калорий - {calories} ккал.")

    await state.finish()

@dp.message_handler(text=['Информация'])
async def info(message):
    print("Запрос инфо")
    await message.answer('Этот бот помогает рассчитать калории')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
