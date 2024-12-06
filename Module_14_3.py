from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API = 'апиапи'

bot = Bot(token=API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Состояния для пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


# Начальная функция с главной клавиатурой
@dp.message_handler(Command('start'))
async def start(message: types.Message):
    # Основное меню с кнопками
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Рассчитать")
    button2 = KeyboardButton("Информация")
    button3 = KeyboardButton("Купить")
    keyboard.add(button1, button2, button3)
    await message.answer("Выберите опцию:", reply_markup=keyboard)


# Функция для обработки кнопки 'Рассчитать'
@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    inline_kb = InlineKeyboardMarkup()
    inline_kb.add(InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'))
    inline_kb.add(InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


# Функция для обработки кнопки 'Информация'
@dp.message_handler(lambda message: message.text == 'Информация')
async def info(message: types.Message):
    await message.answer(text='Привет! Я бот, помогающий твоему здоровью!')


# Обработка Inline меню формул
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        'Формула Миффлина-Сан Жеора для расчёта калорий:\n'
        'Мужчины: 10 × вес (кг) + 6.25 × рост (см) − 5 × возраст (г) + 5\n'
        'Женщины: 10 × вес (кг) + 6.25 × рост (см) − 5 × возраст (г) − 161'
    )
    await call.answer()


# Выбор пола для расчёта калорий
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_gender(call: types.CallbackQuery):
    await UserState.sex.set()
    inline_kb = InlineKeyboardMarkup()
    inline_kb.add(InlineKeyboardButton('Мужчина', callback_data='male'))
    inline_kb.add(InlineKeyboardButton('Женщина', callback_data='female'))
    await call.message.answer("Выберите пол:", reply_markup=inline_kb)
    await call.answer()


# Установка возраста
@dp.callback_query_handler(lambda call: call.data in ['male', 'female'], state=UserState.sex)
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(sex=call.data)
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")
    await call.answer()


# Установка роста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer("Введите свой рост:")


# Установка веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer("Введите свой вес:")


# Расчёт калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    sex = data['sex']

    if sex == 'male':
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
    else:
        calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваши калории: {calories:.2f}")
    await state.finish()


# Функция обработки кнопки 'Купить'
@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    # Отображение продуктов с описаниями
    for i in range(1, 5):
        await message.answer_photo(
            photo=f"https://via.placeholder.com/150?text=Product{i}",  # Заглушка для изображения
            caption=f"Название: Product{i} | Описание: описание {i} | Цена: {i * 100}"
        )

    # Inline клавиатура для выбора продукта
    inline_kb = InlineKeyboardMarkup()
    for i in range(1, 5):
        inline_kb.add(InlineKeyboardButton(f"Product{i}", callback_data="product_buying"))
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb)


# Callback хэндлер для покупки продукта
@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)