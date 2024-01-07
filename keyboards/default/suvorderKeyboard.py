from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

SuvOrderMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒Savat"),
        ],
        [
            KeyboardButton(text="Ortga"),
        ],
    ],
    resize_keyboard=True
)