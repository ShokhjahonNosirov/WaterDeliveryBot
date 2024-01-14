from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.productKeyboard import menuProduct
from keyboards.default.suvKeyboard import menuSuv
from states.personalData import PersonalData

from loader import dp, db


@dp.message_handler(text='🛒Savat')
async def send_link(message: Message):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    added_buttons = set()  # to not repeat the same button
    msg = "<b>🛒Savat:</b>\n\n"
    print(db.get_suv(message.from_user.id)[0])
    suv = db.get_suv(message.from_user.id)[0]
    if suv and suv is not None:
        keyboard.add(KeyboardButton("🚚 Buyurtma berish"))
        added_buttons.add("🚚 Buyurtma berish")
        keyboard.add(KeyboardButton("➖ Suvni o'chirish"))
        msg += f"<b>-Suv</b>\n\n{suv}\n\n"  # 1-savat manimcha shu yerda tugayapti
    # print(suv)
    pompa = db.get_pompa(message.from_user.id)[0]
    # print(pompa)
    if pompa and pompa is not None:
        if "🚚 Buyurtma berish" not in added_buttons:
            keyboard.add(KeyboardButton("🚚 Buyurtma berish"))
        keyboard.add(KeyboardButton("➖ Pompani o'chirish"))
        msg += f"<b>-Pompa</b>\n\n{pompa}\n\n"
    if msg != "<b>🛒Savat:</b>\n\n":
        keyboard.add(KeyboardButton("Ortga"))
        await message.answer(msg, reply_markup=keyboard)
    else:
        keyboard.add(KeyboardButton("Ortga"))
        await message.answer(f"Savat bo'sh", reply_markup=keyboard)


@dp.message_handler(text="➖ Suvni o'chirish")
async def send_link(message: Message):
    db.delete_suv(id=message.from_user.id)
    await message.answer(f"Suv o'chirildi", reply_markup=menuProduct)


@dp.message_handler(text="➖ Pompani o'chirish")
async def send_link(message: Message):
    db.delete_pompa(id=message.from_user.id)
    await message.answer(f"Pompa o'chirildi", reply_markup=menuProduct)




# Pastdagi hech narsa

# @dp.message_handler(text='Ortga')
# async def send_link(message: Message):
#     await message.answer('Siz ortga qaytdingiz', reply_markup=menuProduct)
