import os
API_TOKEN = os.getenv("VK_API_TOKEN")

from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler


api = API(API_TOKEN)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
