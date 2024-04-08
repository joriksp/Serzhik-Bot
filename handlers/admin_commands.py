from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from filters.is_admin import IsAdmin
import config

router = Router()

@router.message(Command('check'), IsAdmin(config.ADMIN_IDS))
async def check(message: Message):
    print(message.chat.id)
    await message.delete()

@router.channel_post(Command('check'))
async def check(message: Message):
    print(message.chat.id)
    await message.delete()