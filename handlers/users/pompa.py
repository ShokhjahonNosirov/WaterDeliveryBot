from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.productKeyboard import menuProduct
from keyboards.default.pompaKeyboard import menuPompa
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.pompaState import PompaState
from keyboards.default.suvorderKeyboard import SuvOrderMenu


from loader import dp, db


@dp.message_handler(text='🅿️ Pompa', state=None)
async def send_link(message: Message):
    photo_id_pompa = 'AgACAgIAAxkBAAIKXmKsCA7FDKwjS28OBETTWs4NjVgiAAJZwDEbdsZgScLNBahtZn_LAQADAgADcwADJAQ'
    await message.answer_photo(photo_id_pompa, caption="*Elektron pompa* \n\nNarxi: 70000.00 so'm \n\n🔻Mahsulot haqida:\n✅USB quvvatlagich\n✅ Foydalanishga qulay \n✅ Navoiy bo'ylab yetkazib berish bepul.", parse_mode='Markdown', reply_markup = menuPompa)
    await message.answer("Miqdorni tanlang yoki kiriting", reply_markup=menuPompa)
    # await message.answer("123", reply_markup=menuSuv)
    await PompaState.pompa.set()


@dp.message_handler(text='Ortga', state=PompaState.pompa)
async def send_link(message: Message, state: FSMContext):
    await message.answer('Siz ortga qaytdingiz', reply_markup=menuProduct)
    await state.finish()
    await PompaState.pompa.set()  # Buni qayta yoqqanimizni sababi bor edi, lekin hoz esimdan chiqdi
    await state.finish()  # shu ortga to'g'ri ishlashi uchun yoqilgan edi


@dp.message_handler(state=PompaState.pompa)
async def send_link(message: Message, state: FSMContext):
    if message.text.isdigit(): # != "Savat" or message.text != "Boshiga":
        print("Xato qiymat kiritildi", message.text)
        await message.answer(
            f"Savatga qo'shildi: \n\n<b>-Pompa</b> \n\n70.000*{int(message.text)}=<b>{70000 * int(message.text)}</b> so'm \n\nBuyurtma berish uchun 🛒Savat tugmasini bosing!\n\nQo'shimcha mahsulotlar sotib olish uchun Ortga tugmasini bosing.",
            reply_markup=SuvOrderMenu)
        pompa_zakaz = f"70.000*{int(message.text)}=<b>{70000 * int(message.text)}</b> so'm"
        db.add_savat_pompa(pompa=pompa_zakaz, id=message.from_user.id)
        await state.finish()
    else:
        await state.finish()






# @dp.message_handler(text='Boshiga', state=SuvState.suv)
# async def send_link(message: Message, state: FSMContext):
#     await message.answer("Kerakli bo'limni tanlang", reply_markup=menu)
#     await state.finish()