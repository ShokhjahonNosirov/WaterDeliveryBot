from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

SavatMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚚 Buyurtma berish"),
        ],
        [
            KeyboardButton(text="Suvni o'chirish"),
        ],
        [
            KeyboardButton(text="Pompani o'chirish"),
        ],
        [
            KeyboardButton(text="Ortga"),
        ],
    ],
    resize_keyboard=True
)