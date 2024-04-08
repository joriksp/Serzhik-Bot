from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import inline
from filters.chat_types import IsGroup

router = Router()

@router.message(Command('start', 'help'), IsGroup())
async def start(message: Message):
    await message.answer(f'''
Это бот службы поддержки канала <i>Сергей Ипполитович</i>. Здесь ты можешь обратиться к администраторам со своим предложением.''', reply_markup=inline.main_group)