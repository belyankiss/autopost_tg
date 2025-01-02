from aiogram import Bot
from pydantic.v1 import BaseModel, root_validator


class Autopost:
    def __init__(self, bot: Bot, from_chat_id, to_chat_id):
        """

        :param bot: Bot - use Bot from aiogram with token bot from BotFather
        :param from_chat_id: int
        :param to_chat_id: int
        """
        self.bot = bot
        self.from_chat_id: int | None = from_chat_id
        self.to_chat_id: int | None = to_chat_id

    async def send(self, message_id: int):
        await self.bot.forward_message(chat_id=self.to_chat_id, from_chat_id=self.from_chat_id, message_id=message_id)



