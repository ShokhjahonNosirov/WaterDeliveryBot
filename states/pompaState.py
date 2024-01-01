from aiogram.dispatcher.filters.state import StatesGroup, State

# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PompaState(StatesGroup):
    pompa = State()
