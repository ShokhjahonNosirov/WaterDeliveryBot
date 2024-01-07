from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuSuv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
        ],
        [
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6"),
        ],
        [
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9"),
        ],
        [
            KeyboardButton(text="Ortga"),
        ]
    ],
    resize_keyboard=True
)