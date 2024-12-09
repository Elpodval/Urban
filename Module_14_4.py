from crud_functions import *
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API = '7450150397:AAH2Uhs_GHvWJ1D_4JU2NjXjDl1ziiUFnwE'

bot = Bot(token=API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных
initiate_db()
populate_products()  # Добавляем тестовые данные, если таблица пустая
all_products = get_all_products()  # Получаем список всех продуктов


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


# Функция для обработки кнопки 'Купить'
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)