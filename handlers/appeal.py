from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import MakeAppeal
from keyboards.builders import profile
from keyboards.reply import rmk
from keyboards import inline

import config

router = Router()

@router.callback_query(F.data == "appeal")
async def appeal(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')

    await state.set_state(MakeAppeal.name)

    await callback.message.answer(
        "👋 Для начала, представьтесь",
        reply_markup=profile(callback.from_user.first_name)
    )

@router.message(MakeAppeal.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(MakeAppeal.title)
    
    await message.answer(
        "📖 Введите тему обращения",
        reply_markup=rmk
    )

@router.message(MakeAppeal.title)
async def form_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)

    await state.set_state(MakeAppeal.message)

    await message.answer(
        "💬 Теперь напишите текст обращения"
    )

@router.message(MakeAppeal.message)
async def form_message(message: Message, state: FSMContext):
    await state.update_data(message=message.text)

    data = await state.get_data()
    
    await message.answer(
        f"✅ Обращение составлено\n\n<b>Тема</b>: <i>{data['title']}</i>\n<b>Текст</b>: <i>{data['message']}</i>\n\n<b>Отправитель</b>: <i>{data['name']}</i>",
        reply_markup=inline.send_appeal
    )

@router.callback_query(F.data == "sendAppeal")
async def send_appeal(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Обращение отправлено!")

    await callback.message.edit_text("✅ Отправлено")

    data = await state.get_data()
    await state.clear()

    for admin in config.ADMIN_IDS:
        await callback.bot.send_message(chat_id=admin, text=f"▶️ Новое обращение\n\n<b>Тема</b>: <i>{data['title']}</i>\n<b>Текст</b>: <i>{data['message']}</i>\n\n<b>Отправитель</b>: <i>{data['name']}</i>\n<b>Юз</b>: @{callback.from_user.username}")

@router.callback_query(F.data == "cancelAppeal")
async def send_appeal(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Обращение отменено")

    await callback.message.edit_text("❌ Отменено")
    await state.clear()
    