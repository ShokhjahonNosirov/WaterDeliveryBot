from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.productKeyboard import menuProduct
from keyboards.default.pompaKeyboard import menuPompa
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.pompaState import PompaState

from loader import dp


@dp.message_handler(text='🅿️ Pompa', state=None)
async def send_link(message: Message):
    photo_id_pompa = 'AgACAgIAAxkBAAIKXmKsCA7FDKwjS28OBETTWs4NjVgiAAJZwDEbdsZgScLNBahtZn_LAQADAgADcwADJAQ'
    await message.answer_photo(photo_id_pompa, caption="*Elektron pompa* \n\nNarxi: 70000.00 so'm \n\n🔻Mahsulot haqida:\n✅USB quvvatlagich\n✅ Foydalanishga qulay \n✅ Navoiy bo'ylab yetkazib berish bepul.", parse_mode='Markdown', reply_markup = menuPompa)
    # await message.answer("123", reply_markup=menuSuv)
    await PompaState.pompa.set()


@dp.message_handler(text='pompa nimadir', state=PompaState.pompa)
async def send_link(message: Message, state: FSMContext):
    await message.answer("132", reply_markup=menuPompa)
    await state.finish()


@dp.message_handler(text='pompa nimadir2', state=PompaState.pompa)
async def send_link(message: Message, state: FSMContext):
    await message.answer("456", reply_markup=ReplyKeyboardRemove())
    await state.finish()

# @dp.message_handler(text='Boshiga', state=SuvState.suv)
# async def send_link(message: Message, state: FSMContext):
#     await message.answer("Kerakli bo'limni tanlang", reply_markup=menu)
#     await state.finish()

@dp.message_handler(text='Ortga', state=PompaState.pompa)
async def send_link(message: Message, state: FSMContext):
    await message.answer('Siz ortga qaytdingiz', reply_markup=menuProduct)
    await state.finish()



