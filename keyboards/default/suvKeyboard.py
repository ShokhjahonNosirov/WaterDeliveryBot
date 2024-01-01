from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuSuv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="suv nimadir"),
            KeyboardButton(text="suv nimadir 2"),
        ],

        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ]
    ],
    resize_keyboard=True
)