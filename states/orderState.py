from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
# ism-familiya so'ralmaydi, hurmatli mijoz deb murojaat qilinadi
class OrderState(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    # bittasidan o'tsa ikkinchiga o'tadi
    narx = State()
    contact = State()  # tel
    manzil = State()
    idish = State()  # Tel raqami
    izoh = State()
    final = State()
    # o'ziga message jo'natib buyurtmani tasdiqlash so'raladi