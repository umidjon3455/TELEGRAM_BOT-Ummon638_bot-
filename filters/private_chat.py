from collections.abc import Sequence

from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatPrivateFilter(BaseFilter):
    """Allow updates only from the configured Telegram chat types."""

    def __init__(self, chat_type: str | Sequence[str]):
        self.chat_types = {chat_type} if isinstance(chat_type, str) else set(chat_type)

    async def __call__(self, message: Message) -> bool:
        return message.chat.type in self.chat_types
