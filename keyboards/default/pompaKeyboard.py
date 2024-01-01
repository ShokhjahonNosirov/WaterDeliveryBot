from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPompa = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="pompa nimadir"),
            KeyboardButton(text="pompa nimadir 2"),
        ],

        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ]
    ],
    resize_keyboard=True
)