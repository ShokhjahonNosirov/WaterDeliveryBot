import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startKeyboard import menuStart
from keyboards.default.menuKeyboard import menu

from data.config import ADMINS
from loader import dp, db, bot
from aiogram.dispatcher.filters import Command


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    all_users = db.get_all_ids()
    await message.answer(f"Salom, {message.from_user.full_name}!\n", reply_markup=menu)

    # Foydalanuvchini bazaga qo'shamiz
    user_id = message.from_user.id
    if (user_id,) not in all_users:
        try:
            db.add_user(id=message.from_user.id,
                        name=name)
            count = db.count_users()[0]
            msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=-4166714643, text=msg)
        except sqlite3.IntegrityError as err:
            pass
    # await bot.send_message(chat_id=ADMINS[0], text=err)


@dp.message_handler(Command("users"))
async def user_number(message: types.Message):
    count = db.count_users()[0]
    await bot.send_message(chat_id=-4166714643, text=f"Sizda mavujud foydalanuvchilar soni {count}")
