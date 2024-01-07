from aiogram.dispatcher.filters.state import StatesGroup, State

# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class SuvState(StatesGroup):
    suv = State()
    suv_savat = State()



