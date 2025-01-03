import asyncio

from aiogram import Bot

from autopost import Autopost

bot = Bot(token=)
autopost = Autopost(bot=bot, from_chat_id=-1002450289099, to_chat_id=-1002083546431)

if __name__ == '__main__':
    asyncio.run(autopost.send(message_id=103))
