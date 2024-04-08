from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.builders import profile
from keyboards import inline

import config

router = Router()

@router.callback_query(F.data == "add_request")
async def appeal(callback: CallbackQuery):
    await callback.answer('')

    chat_member = await callback.bot.get_chat_member(config.CHANNEL_ID, callback.from_user.id)

    if chat_member.status == 'left':
        await callback.message.answer(
            "✅ Запрос на добавление отправлен"
        )

        for admin in config.ADMIN_IDS:
            await callback.bot.send_message(chat_id=admin, text=f"➕ Запрос на добавление: @{callback.from_user.username}")
    else:
        await callback.message.answer(
            "💫 Вы уже являетесь участником"
        )