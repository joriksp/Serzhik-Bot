from aiogram import Router, F
from aiogram.types import Message

from keyboards import reply, inline, builders, fabrics
from data.subloader import get_json

router = Router()

@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    smiles = await get_json("smiles.json")

    if msg == 'ссылки':
        await message.answer('Ссылки', reply_markup=inline.links)
    elif msg == 'спец. кнопки':
        await message.answer('Кнопки', reply_markup=reply.spec)
    elif msg == 'калькулятор':
        await message.answer('Калькулятор', reply_markup=builders.calc())
    elif msg == 'смайлики':
        await message.answer(f'{smiles[0][0]} <i>{smiles[0][1]}</i>', reply_markup=fabrics.paginator())