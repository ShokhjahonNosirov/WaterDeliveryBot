import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
from aiogram.utils.exceptions import TelegramAPIError


# @dp.message_handler(text="/allusers", user_id=ADMINS)
# async def get_all_users(message: types.Message):
#     users = db.select_all_users()
#     print(users[0][0])
#     await message.answer(users)

block = set()


@dp.message_handler(text="/mijozlarim", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        try:
            await bot.send_message(chat_id=user_id, text="Kuningiz hayrli o'tsin")
            await asyncio.sleep(0.05)   
        except Exception as e:
            if "Forbidden: bot was blocked by the user" in str(e):
                db.delete_user(user_id)
                # block.add(user_id)
                # print(block)
    count = db.count_users()[0]
    msg = f"Bazada ayni damda {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=-4128658827, text=msg)



