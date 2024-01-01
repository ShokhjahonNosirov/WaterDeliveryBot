from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuProduct = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Suv"),
            KeyboardButton(text="Pompa"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],
    ],
    resize_keyboard=True
)