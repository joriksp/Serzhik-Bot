from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from keyboards import reply

from filters.is_admin import IsAdmin
from filters.is_digit import IsDigit

router = Router()

@router.message(Command('start', 'help'), IsAdmin([1494732557]))
async def start(message: Message):
    await message.answer(f'Hello <b>{message.from_user.first_name}</b>!', reply_markup=reply.main)

@router.message(Command('pay'), IsDigit())
async def pay(message: Message, command: CommandObject):
    await message.answer(f"Вы успешно оплатили товар на сумму <b>{command.args}</b>!")