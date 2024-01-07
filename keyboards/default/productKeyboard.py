from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuProduct = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💧 Suv"),
            KeyboardButton(text="🅿️ Pompa"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],
        [
            KeyboardButton(text="🛒Savat"),
        ],
    ],
    resize_keyboard=True
)