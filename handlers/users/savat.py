from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from states.orderState import OrderState
from keyboards.default.productKeyboard import menuProduct
from keyboards.default.suvKeyboard import menuSuv
from states.personalData import PersonalData

from loader import dp, db


@dp.message_handler(text='🛒Savat')
async def send_link(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    added_buttons = set()  # to not repeat the same button
    msg = "<b>🛒Savat:</b>\n\n"
    # print(db.get_suv(message.from_user.id)[0])
    suv = db.get_suv(message.from_user.id)[0]

    if suv and suv is not None:
        keyboard.add(KeyboardButton("🚚 Buyurtma berish"))
        added_buttons.add("🚚 Buyurtma berish")
        keyboard.add(KeyboardButton("➖ Suvni o'chirish"))
        msg += f"<b>-Suv</b>\n\n{suv}\n\n"  # 1-savat manimcha shu yerda tugayapti
        # await OrderState.contact.set()
    # print(suv)
    pompa = db.get_pompa(message.from_user.id)[0]
    # print(pompa)
    if pompa and pompa is not None:
        if "🚚 Buyurtma berish" not in added_buttons:
            keyboard.add(KeyboardButton("🚚 Buyurtma berish"))
        keyboard.add(KeyboardButton("➖ Pompani o'chirish"))
        msg += f"<b>-Pompa</b>\n\n{pompa}\n\n"
    await OrderState.narx.set()
    if msg != "<b>🛒Savat:</b>\n\n":
        keyboard.add(KeyboardButton("Ortga"))
        await message.answer(msg, reply_markup=keyboard)
    else:
        keyboard.add(KeyboardButton("Ortga"))
        await message.answer(f"Savat bo'sh", reply_markup=keyboard)



@dp.message_handler(text="➖ Suvni o'chirish", state=OrderState.narx)
async def send_link(message: Message, state: FSMContext):
    db.delete_suv(id=message.from_user.id)
    await message.answer(f"Suv o'chirildi", reply_markup=menuProduct)
    await state.finish()


@dp.message_handler(text="➖ Pompani o'chirish", state=OrderState.narx)
async def send_link(message: Message, state: FSMContext):
    db.delete_pompa(id=message.from_user.id)
    await message.answer(f"Pompa o'chirildi", reply_markup=menuProduct)
    await state.finish()


@dp.message_handler(text="Ortga", state=OrderState.narx)
async def send_link(message: Message, state: FSMContext):
    await message.answer("Siz Ortga qaytdingiz", reply_markup=menuProduct)
    await state.finish()

# Pastdagi hech narsa

# @dp.message_handler(text='Ortga')
# async def send_link(message: Message):
#     await message.answer('Siz ortga qaytdingiz', reply_markup=menuProduct)
