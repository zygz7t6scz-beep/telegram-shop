from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Каталог"),
            KeyboardButton(text="🛒 Корзина"),
        ],
        [
            KeyboardButton(text="📦 Мои заказы"),
            KeyboardButton(text="☎️ Поддержка"),
        ],
    ],
    resize_keyboard=True,
)
