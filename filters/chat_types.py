from typing import Any

from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsGroup(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type in ["group", "supergroup"]

class IsChannel(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'channel'

class IsPrivate(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'private'