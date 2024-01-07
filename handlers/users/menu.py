from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.productKeyboard import menuProduct
from keyboards.default.suvKeyboard import menuSuv
from states.personalData import PersonalData

from loader import dp, db

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kerakli bo'limni tanlang", reply_markup=menu)

@dp.message_handler(text='🎁 Aksiyalar')
async def send_link(message: Message):
    await message.answer("✔️ Boshlang'ich to'lov(zalog) so'ralmaydi\n✔️ Yetkazib berish bepul")

@dp.message_handler(text='📦 Mahsulotlar')
async def send_link(message: Message):
    await message.answer("Mahsulotni tanlang:", reply_markup=menuProduct)

@dp.message_handler(text="📞 Biz bilan bog'lanish")
async def send_link(message: Message):
    await message.answer("Kontaktlar:\n+998930351011\n+998992851011\n\nSizga yordam berishdan doim mamnunmiz)", reply_markup=menu)

@dp.message_handler(text='📢 Bizni kuzatib boring')
async def send_link(message: Message):
    await message.answer("Instagram: shifosuv\nFacebook: shifosuv uz\nWebsite: shifosuv.uz", reply_markup=menu)

@dp.message_handler(text='Boshiga')
async def send_link(message: Message):
    await message.answer("Kerakli bo'limni tanlang", reply_markup=menu)

@dp.message_handler(text='Ortga')
async def send_link(message: Message):
    await message.answer('Siz ortga qaytdingiz', reply_markup=menu)








