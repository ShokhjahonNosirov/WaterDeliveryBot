from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.productKeyboard import menuProduct
from keyboards.default.suvKeyboard import menuSuv
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.suvState import SuvState

from loader import dp


@dp.message_handler(text='Suv', state=None)
async def send_link(message: Message):
    photo_id_suv = 'AgACAgIAAxkBAAIKYGKsCbY_tvwWHQtbPRU-HGUqk-grAAJawDEbdsZgScMW9g7oj0yvAQADAgADcwADJAQ'
    await message.answer_photo(photo_id_suv, caption="*Shifo Suv - 18.9 L* \n\nNarxi: 10 000 so'm \n\n🔻Mahsulot haqida:\n\n💧🕋 Artezian suvi 7 qirrali maxsus filtrda koreya texnologiyasi asosida o'n ikki bosqichli maxsus filtrda tozalanib, qo'shimcha ravishda minerallashtiriladi. Minerallashtirish jarayonida inson tanasi uchun zarur bo'lgan kalsiy, ftor, yod, kaliy, magniy, natriy bilan suv tarkibi boyitiladi. Bundan tashqari, shifo suv artezian suvi filtrlardan o'tkazilib tayyor ichimlik suv holiga kelgach,  muqaddas Makka shahridan keltirilgan 'Zam-zam' suvi qo'shiladi.\n\n🚚 Navoiy bo'ylab yetkazib berish bepul.", parse_mode='Markdown', reply_markup = menuSuv)
    # await message.answer("123", reply_markup=menuSuv)
    await SuvState.suv.set()


@dp.message_handler(text='suv nimadir', state=SuvState.suv)
async def send_link(message: Message, state: FSMContext):
    await message.answer("132", reply_markup=menuSuv)
    await state.finish()


@dp.message_handler(text='suv nimadir2', state=SuvState.suv)
async def send_link(message: Message, state: FSMContext):
    await message.answer("456", reply_markup=ReplyKeyboardRemove())
    await state.finish()

# @dp.message_handler(text='Boshiga', state=SuvState.suv)
# async def send_link(message: Message, state: FSMContext):
#     await message.answer("Kerakli bo'limni tanlang", reply_markup=menu)
#     await state.finish()

@dp.message_handler(text='Ortga', state=SuvState.suv)
async def send_link(message: Message, state: FSMContext):
    await message.answer('Siz ortga qaytdingiz', reply_markup=menuProduct)
    await state.finish()