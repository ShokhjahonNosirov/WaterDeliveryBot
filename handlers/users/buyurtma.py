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


@dp.message_handler(text='🚚 Buyurtma berish', state=OrderState.narx)
async def send_link(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # final_value = 0
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
    final_value = suv_value + pompa_value
    tel = db.get_tel(message.from_user.id)[0]
    if final_value != 0:
        await state.update_data(  # line 21 bn 1 xil ish qiladi
            {"price": final_value}
        )
        if tel and tel is not None:
            keyboard.add(KeyboardButton("✅"))
            keyboard.add(KeyboardButton("📞 Tel raqamini yuborish", request_contact=True))
            keyboard.add(KeyboardButton("Ortga"))
            msg1 = f"<b>🚚 Buyurtma berish:</b>\n\nBuyurtma narxi {final_value} so'm. \n\nTelefon raqamingiz: {tel}\n" \
                   f"Agar ma'lumot to'g'ri bo'lsa ✅ tugmasini bosing.\n\nAgar raqamingiz o'zgargan bo'lsa " \
                   f"Telefon raqamingizni +998887654321 formatida kiriting yoki 📞 Tel raqamini yuborish tugmasini bosing."
            await message.answer(msg1, reply_markup=keyboard)

        else:
            keyboard.add(KeyboardButton("📞 Tel raqamini yuborish", request_contact=True))
            msg2 = f"<b>🚚 Buyurtma berish:</b>\n\nBuyurtma narxi {final_value} so'm. \n\nTelefon raqamingizni +998887654321 formatida kiriting yoki quyidagi tugmani bosing."
            await message.answer(msg2, reply_markup=keyboard)
        # print(message.answer(message.from_user.id))
        # await state.finish()
        # await OrderState.contact.set()
        keyboard.add(KeyboardButton("Ortga"))
        await OrderState.next()
        # return final
    else:
        await state.finish()
        await message.answer("Savat bo'sh", reply_markup=menuProduct)

    if message.text == "Ortga":
        await message.answer("Siz Ortga qaytdingiz", reply_markup=menuProduct)
        await state.finish()

# msg = "<b>Quyidagi ma'lumotlar qabul qilindi:</b> \n"


@dp.message_handler(content_types=[types.ContentType.CONTACT, types.ContentType.TEXT], state=OrderState.contact)
async def send_link_contact(message: Message, state: FSMContext):
    msg = "<b>Quyidagi ma'lumotlar qabul qilindi:</b> \n"
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # state_data = await state.get_data()
    # final_value = state_data.get("final", 0)
    # print(final)
    if message.text == "Ortga":
        await message.answer("Siz Ortga qaytdingiz", reply_markup=menuProduct)
        await state.finish()
    else:
        if message.content_type == types.ContentType.CONTACT:
            db.add_tel(tel=message.contact.phone_number, id=message.from_user.id)

            await state.update_data(
                {"tel": message.contact.phone_number}
            )
            # print(type(message.contact.phone_number))
        elif message.text == "✅":
            tel = db.get_tel(message.from_user.id)[0]
            await state.update_data(
                {"tel": tel}
            )
        elif message.content_type == types.ContentType.TEXT:
            db.add_tel(tel=message.text, id=message.from_user.id)
            await state.update_data(
                {"tel": message.text}
            )
            # print(message.text)
        # await state.finish()
        # msg = f"<b>🚚 Buyurtma berish:</b>\n\nBuyurtma narxi {final} so'm. \n\nTelefon
        # raqamingizni +998887654321 formatida kiriting yoki quyidagi tugmani bosing."
        data = await state.get_data()
        f_narx = data.get("price")
        f_tel = data.get("tel")
        msg = f"{msg}\nBuyurtma narxi: {f_narx} so'm.\nTelefon: {f_tel}\n"
        manzil = db.get_manzil(message.from_user.id)[0]
        if manzil and manzil is not None:
            keyboard.add(KeyboardButton("✅"))
            keyboard.add(KeyboardButton("Ortga"))
            await message.answer(f"{msg}\n🏡Mahalla, Ko'cha, Uy raqami: {manzil} \n Ko'rsatilgan "
                                 f"manzil to'g'ri bo'lsa ✅ tugmasini bosing. \n\nAgar o'zgargan bo'lsa "
                                 f"🏡Mahalla, Ko'cha, Uy raqamini to'liq kiriting.", reply_markup=keyboard)
        else:
            keyboard.add(KeyboardButton("Ortga"))
            await message.answer(f"{msg}\n🏡Mahalla, Ko'cha, Uy raqamini to'liq kiriting", reply_markup=keyboard)
        await state.update_data(
            {"msg": msg}
        )

        await OrderState.next()


@dp.message_handler(state=OrderState.manzil)
async def send_link(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("0️⃣ Idish yo'q"))
    keyboard.add(KeyboardButton("Ortga"))
    if message.text == "Ortga":
        await message.answer("Siz Ortga qaytdingiz", reply_markup=menuProduct)
        await state.finish()
    else:
        if message.text == "✅":
            manzil = db.get_manzil(message.from_user.id)[0]
            await state.update_data(
                {"manzil": manzil}
            )
        else:
            db.add_manzil(manzil=message.text, id=message.from_user.id)
            await state.update_data(
                {"manzil": message.text}
            )
        data = await state.get_data()
        f_manzil = data.get("manzil")
        msg = data.get("msg")
        msg = f"{msg}Manzil: {f_manzil}\n"
        await message.answer(f"{msg}\nQaytadigan idish sonini kiriting.\nIdish bo'lmasa 0️⃣ Idish yo'q tugmasini bosing", reply_markup=keyboard)
        # print(message.text)
        # await state.finish()
        await state.update_data(
            {"msg": msg}
        )
        await OrderState.next()


@dp.message_handler(state=OrderState.idish)
async def send_link(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Izoh yo'q"))
    keyboard.add(KeyboardButton("Ortga"))
    if message.text == "Ortga":
        await message.answer("Siz Ortga qaytdingiz", reply_markup=menuProduct)
        await state.finish()
    else:
        await state.update_data(
            {"idish": message.text}
        )
        db.add_idish(idish=message.text, id=message.from_user.id)
        data = await state.get_data()
        f_idish = data.get("idish")
        msg = data.get("msg")
        msg = f"{msg}Qaytadigan idish soni: {f_idish}"
        await state.update_data(
            {"msg": msg}
        )
        await message.answer(f"{msg}\n\nQo'shimcha izoh bo'lsa yozing."
                             f"\nIzhoh mavjud bo'lmasa Izoh yo'q tugmasini bosing.", reply_markup=keyboard)

        # print(message.text)
        # await state.finish()
        await OrderState.next()


@dp.message_handler(state=OrderState.izoh)
async def send_link(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("✅Buyurtmani tasdiqalash"))
    keyboard.add(KeyboardButton("Ortga"))
    if message.text == "Ortga":
        await message.answer("Siz Ortga qaytdingiz", reply_markup=menuProduct)
        await state.finish()
    else:
        db.add_izoh(izoh=message.text, id=message.from_user.id)
        await state.update_data(
            {"izoh": message.text}
        )
        # suv = db.get_suv(message.from_user.id)[0]
        data = await state.get_data()
        f_izoh = data.get("izoh")
        msg = data.get("msg")
        msg = f"{msg}\nIzoh: {f_izoh}\n"
        await state.update_data(
            {"msg": msg}
        )
        await message.answer(msg, reply_markup=keyboard)
        await OrderState.next()


@dp.message_handler(state=OrderState.final)
async def send_link(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Ortga"))
    if message.text == "Ortga":
        await message.answer("Siz Ortga qaytdingiz", reply_markup=menuProduct)
        await state.finish()
    else:
        pompa = db.get_pompa(message.from_user.id)[0]
        suv = db.get_suv(message.from_user.id)[0]
        await message.answer("Raxmat, buyurtmaningiz qabul qilindi.", reply_markup=keyboard)
        data = await state.get_data()
        msg = data.get("msg")
        await bot.send_message(chat_id='-4166714643', text=msg + f"\nSuv - {suv}\nPompa - {pompa}")
        db.delete_suv(id=message.from_user.id)
        db.delete_pompa(id=message.from_user.id)
        await state.finish()
# https://github.com/anvarnarz/mukammal-bot-paid/blob/location_contact/handlers/users/contact_handler.py
# shu darsni ko'r q  anday kontakt so'rashni o'rgan.
