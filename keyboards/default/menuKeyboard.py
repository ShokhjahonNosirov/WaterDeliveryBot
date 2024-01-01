from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📦 Mahsulotlar'),
            KeyboardButton(text='🎁 Aksiyalar'),
        ],
        [
            KeyboardButton(text="📞 Biz bilan bog'lanish"),
            KeyboardButton(text='📢 Bizni kuzatib boring'),
        ]
    ],
    resize_keyboard=True
)