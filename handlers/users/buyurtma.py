from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.productKeyboard import menuProduct
from aiogram.dispatcher import FSMContext

from keyboards.default.productKeyboard import menuProduct
from keyboards.default.suvKeyboard import menuSuv
from states.orderState import OrderState

from loader import dp, db


@dp.message_handler(text='🚚 Buyurtma berish')
async def send_link(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("📞 Tel raqamini yuborish"))
    keyboard.add(KeyboardButton("Ortga"))
    suv_value = 0  # bu else ni o'rniga
    pompa_value = 0
    pompa = db.get_pompa(message.from_user.id)[0]
    suv = db.get_suv(message.from_user.id)[0]
    if suv and suv is not None:
        suv_value = int(suv.split("<b>")[1][:-9])
        print(suv_value)
    if pompa and pompa is not None:
        pompa_value = int(pompa.split("<b>")[1][:-9])
        print(pompa_value)
    final = suv_value+pompa_value
    if final != 0:
        msg = f"<b>🚚 Buyurtma berish:</b>\n\nBuyurtma narxi {final} so'm. \n\nTelefon raqamingizni +998887654321 formatida kiriting yoki quyidagi tugmani bosing."
        await message.answer(msg, reply_markup=keyboard)
        await OrderState.contact.set()
    else:
        await message.answer("Savat bo'sh", reply_markup=menuProduct)

@dp.message_handler(state=OrderState.contact)
async def send_link(message: Message, state: FSMContext):
    if message.text == "📞 Tel raqamini yuborish":
        pass
# https://github.com/anvarnarz/mukammal-bot-paid/blob/location_contact/handlers/users/contact_handler.py
# shu darsni ko'r qanday kontakt so'rashni o'rgan.