from aiogram.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💬 Обратиться к администраторам', callback_data='appeal')
        ],
        [
            InlineKeyboardButton(text='⭐ Запрос на добавление', callback_data='add_request')
        ]
    ]
)

main_group = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💬 Обратиться к администраторам', url="tg://resolve?domain=sergey_channelbot")
        ]
    ]
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

send_appeal = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛫 Отправить", callback_data="sendAppeal")
        ],
        [
            InlineKeyboardButton(text="❌ Отменить", callback_data="cancelAppeal")
        ]
    ]
)
