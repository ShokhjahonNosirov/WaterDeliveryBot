from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.productKeyboard import menuProduct
from keyboards.default.suvKeyboard import menuSuv
from states.personalData import PersonalData

from loader import dp, db


@dp.message_handler(text='🛒Savat')
async def send_link(message: Message):
    msg = "<b>🛒Savat:</b>\n\n"
    suv = db.get_suv(message.from_user.id)[0]
    if suv and suv is not None:
        msg += f"<b>-Suv</b>\n\n{suv}\n\n"  # 1-savat manimcha shu yerda tugayapti
    # print(suv)
    pompa = db.get_pompa(message.from_user.id)[0]
    # print(pompa)
    if pompa and pompa is not None:
        msg += f"<b>-Pompa</b>\n\n{pompa}\n\n"
    if msg != "<b>🛒Savat:</b>\n\n":
        await message.answer(msg, reply_markup=menu)
    else:
        await message.answer(f"Savat bo'sh", reply_markup=menu)