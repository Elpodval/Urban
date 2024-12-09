from crud_functions import *
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from homework.Module_13.module_13_6 import UserState

API = '7450150397:AAH2Uhs_GHvWJ1D_4JU2NjXjDl1ziiUFnwE'

bot = Bot(token=API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных
initiate_db()
populate_products()  # Добавляем тестовые данные
all_products = get_all_products()  # Получаем список всех продуктов


# Состояния для регистрации пользователя
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# Начальная функция с главной клавиатурой
@dp.message_handler(Command('start'))
async def start(message: types.Message):
    # Основное меню с кнопками
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Рассчитать")
    button2 = KeyboardButton("Информация")
    button3 = KeyboardButton("Купить")
    button4 = KeyboardButton("Регистрация")
    keyboard.add(button1, button2, button3, button4)
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    # Используем данные из базы для отображения продуктов
    for product in all_products:
        product_id, title, description, price = product
        with open('product.jpg', "rb") as img:
            await message.answer_photo(
                img,
                caption=f"Название: {title} | Описание: {description} | Цена: {price}"
            )

    # Inline клавиатура для выбора продукта
    inline_kb = InlineKeyboardMarkup()
    for product in all_products:
        product_id, title, _, _ = product
        inline_kb.add(InlineKeyboardButton(f"{title}", callback_data="product_buying"))
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb)


# Callback хэндлер для покупки продукта
@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


# Регистрация: начальный шаг
@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sing_up(message: types.Message):
    await RegistrationState.username.set()
    await message.answer("Введите имя пользователя (только латинский алфавит):")


# Установка имени пользователя
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await RegistrationState.email.set()
        await message.answer("Введите свой email:")


# Установка email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await RegistrationState.age.set()
    await message.answer("Введите свой возраст:")


# Установка возраста
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть числом. Введите ещё раз:")
        return

    await state.update_data(age=int(age))

    # Получение данных из состояния
    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = data['age']

    # Добавление пользователя в базу данных
    add_user(username, email, age)
    await message.answer("Регистрация завершена!")
    await state.finish()

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
