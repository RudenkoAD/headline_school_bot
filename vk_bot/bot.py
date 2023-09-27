from vkbottle import Bot
from vk_bot.config import api, state_dispenser, labeler
from vk_bot.handlers import labelers

for labeler_ in labelers:
    labeler.load(labeler_)

bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)

bot.run_forever()