from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.productKeyboard import menuProduct
from aiogram.dispatcher import FSMContext
from aiogram import types

from keyboards.default.productKeyboard import menuProduct
from keyboards.default.suvKeyboard import menuSuv
from states.orderState import OrderState

from loader import dp, db, bot

final = 0


@dp.message_handler(text='🚚 Buyurtma berish')
async def send_link(message: Message, state: FSMContext):
    global final
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("📞 Tel raqamini yuborish", request_contact=True))
    keyboard.add(KeyboardButton("Ortga"))
    suv_value = 0  # bu else ni o'rniga
    pompa_value = 0
    pompa = db.get_pompa(message.from_user.id)[0]
    suv = db.get_suv(message.from_user.id)[0]
    if suv and suv is not None:
        suv_value = int(suv.split("<b>")[1][:-9])
        # print(suv_value)
    if pompa and pompa is not None:
        pompa_value = int(pompa.split("<b>")[1][:-9])
        # print(pompa_value)
    final = suv_value + pompa_value
    if final != 0:
        msg = f"<b>🚚 Buyurtma berish:</b>\n\nBuyurtma narxi {final} so'm. \n\nTelefon raqamingizni +998887654321 formatida kiriting yoki quyidagi tugmani bosing."
        await message.answer(msg, reply_markup=keyboard)
        # print(message.answer(message.from_user.id))
        # await state.finish()
        await OrderState.contact.set()
        # return final
    else:
        await message.answer("Savat bo'sh", reply_markup=menuProduct)


msg = "<b>Quyidagi ma'lumotlar qabul qilindi:</b> \n"


@dp.message_handler(content_types=[types.ContentType.CONTACT, types.ContentType.TEXT], state=OrderState.contact)
async def send_link_contact(message: Message, state: FSMContext):
    global final, msg
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Ortga"))
    # state_data = await state.get_data()
    # final_value = state_data.get("final", 0)
    # print(final)
    if message.content_type == types.ContentType.CONTACT:
        db.add_tel(tel=message.contact.phone_number, id=message.from_user.id)
        await state.update_data(
            {"narx": final,
             "tel": message.contact.phone_number}
        )
        # print(type(message.contact.phone_number))
    elif message.content_type == types.ContentType.TEXT:
        db.add_tel(tel=message.text, id=message.from_user.id)
        await state.update_data(
            {"narx": final,
             "tel": message.text}
        )
        # print(message.text)
    # await state.finish()
    # msg = f"<b>🚚 Buyurtma berish:</b>\n\nBuyurtma narxi {final} so'm. \n\nTelefon
    # raqamingizni +998887654321 formatida kiriting yoki quyidagi tugmani bosing."
    data = await state.get_data()
    f_narx = data.get("narx")
    f_tel = data.get("tel")
    msg = f"{msg}\nBuyurtma narxi: {f_narx} so'm.\nTelefon: {f_tel}\n"
    await message.answer(f"{msg}\n🏡Mahalla, Ko'cha, Uy raqamini to'liq kiriting", reply_markup=keyboard)
    await OrderState.next()


@dp.message_handler(state=OrderState.manzil)
async def send_link(message: Message, state: FSMContext):
    global msg
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Ortga"))
    db.add_manzil(manzil=message.text, id=message.from_user.id)
    await state.update_data(
        {"manzil": message.text}
    )
    data = await state.get_data()
    f_manzil = data.get("manzil")
    msg = f"{msg}Manzil: {f_manzil}\n"
    await message.answer(f"{msg}\nQaytadigan idish sonini kiriting.", reply_markup=keyboard)
    # print(message.text)
    # await state.finish()
    await OrderState.next()


@dp.message_handler(state=OrderState.idish)
async def send_link(message: Message, state: FSMContext):
    global msg
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Ortga"))
    await state.update_data(
        {"idish": message.text}
    )
    db.add_idish(idish=message.text, id=message.from_user.id)
    data = await state.get_data()
    f_idish = data.get("idish")
    msg = f"{msg}Qaytadigan idish soni: {f_idish}"
    await message.answer(f"{msg}\n\nQo'shimcha izoh bo'lsa yozing."
                         f"\nIzhoh mavjud bo'lmasa ... tugmasini bosing.", reply_markup=keyboard)

    # print(message.text)
    # await state.finish()
    await OrderState.next()


@dp.message_handler(state=OrderState.izoh)
async def send_link(message: Message, state: FSMContext):
    global msg
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Ortga"))
    db.add_izoh(izoh=message.text, id=message.from_user.id)
    await state.update_data(
        {"izoh": message.text}
    )
    # suv = db.get_suv(message.from_user.id)[0]
    data = await state.get_data()
    f_izoh = data.get("izoh")
    msg = f"{msg}\nIzoh: {f_izoh}\n"
    await message.answer(msg, reply_markup=keyboard)
    await bot.send_message(chat_id='your_channel_id', text=msg, reply_markup=keyboard)
    # print(message.text)
    await state.finish()
    # await OrderState.next()
# https://github.com/anvarnarz/mukammal-bot-paid/blob/location_contact/handlers/users/contact_handler.py
# shu darsni ko'r q  anday kontakt so'rashni o'rgan.
