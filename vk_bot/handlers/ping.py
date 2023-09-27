#This is a test handler

from vk_bot.config import labeler

@labeler.message(text="ping")
async def ping_handler(message):
    await message.answer("pong")
