from aiogram.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', url='https://youtube.com'),
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=darkelitt'),
        ]
    ]
)

sub_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подписаться", url="tg://resolve?domain=sergg_68")
        ]
    ]
)