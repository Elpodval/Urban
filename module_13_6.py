from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = 'апиапи'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()  # Добавляем состояние для выбора пола


# Начальная функция
@dp.message_handler(Command('start'))
async def start(message: types.Message):
    # Основное меню с кнопками
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Рассчитать")
    button2 = KeyboardButton("Информация")
    keyboard.add(button1, button2)
    await message.answer("Выберите опцию:", reply_markup=keyboard)


# Функция для обработки кнопки 'Рассчитать'
@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    inline_kb = InlineKeyboardMarkup()
    inline_kb.add(InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'))
    inline_kb.add(InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

@dp.message_handler(lambda message: message.text == 'Информация')
async def info(message):
    await message.answer(text='Привет! Я бот, помогающий твоему здоровью!')


# Функция получения формул
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формула Миффлина-Сан Жеора, '
                              'разработанная группой американских врачей-диетологов '
                              'под руководством докторов Миффлина и Сан Жеора, '
                              'существует в двух вариантах – упрощенном и доработанном '
                              'и выдает необходимое количество килокалорий (ккал) '
                              'в сутки для каждого конкретного человека. '
                              'Упрощенный вариант формулы Миффлина-Сан Жеора: '
                              'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; '
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


# Функция выбора расчёта калорий
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_gender(call: types.CallbackQuery):
    await UserState.sex.set()  # Устанавливаем состояние выбора пола
    inline_kb = InlineKeyboardMarkup()
    inline_kb.add(InlineKeyboardButton('Мужчина', callback_data='male'))
    inline_kb.add(InlineKeyboardButton('Женщина', callback_data='female'))
    await call.message.answer("Выберите пол:", reply_markup=inline_kb)
    await call.answer()


# Функция установки возраста
@dp.callback_query_handler(lambda call: call.data in ['male', 'female'], state=UserState.sex)
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(sex=call.data)  # Сохраняем пол
    await UserState.age.set()  # Устанавливаем состояние возраста
    await call.message.answer("Введите свой возраст:")
    await call.answer()


# Функция установки роста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await UserState.growth.set()  # Устанавливаем состояние роста
    await message.answer("Введите свой рост:")


# Функция установки веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await UserState.weight.set()  # Устанавливаем состояние веса
    await message.answer("Введите свой вес:")


# Функция расчета калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    sex = data['sex']  # Получаем пол

    if sex == 'male':
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
    else:
        calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваши калории: {calories:.2f}")
    await state.finish()  # Завершаем машину состояний


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
