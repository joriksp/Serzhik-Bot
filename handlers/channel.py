from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import inline
from filters.chat_types import IsGroup

import config

router = Router()

@router.channel_post()
async def send_warn(message: Message, bot: Bot):
    await bot.send_message(chat_id=config.CHANNEL_GROUP_ID, text="Просим поддерживать хороший разговор без запреток пж", reply_to_message_id=message.message_id)