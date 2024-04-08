from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import inline
from filters.chat_types import IsPrivate

router = Router()

@router.message(Command('start', 'help'), IsPrivate())
async def start(message: Message):
    await message.answer(f'''
Здравствуй, {message.from_user.first_name}! 👋
                         
Это бот службы поддержки канала <i>Сергей Ипполитович</i>. Здесь ты можешь обратиться к администраторам со своим предложением.

Также, поскольку канал стал закрытым, вы можете отправить запрос на добавление здесь.''', reply_markup=inline.main)