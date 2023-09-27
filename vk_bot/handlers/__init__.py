from vk_bot.handlers.chat import chat_labeler
from vk_bot.handlers.admin import admin_labeler
from vk_bot.handlers.ping import labeler
# Если использовать глобальный лейблер, то все хендлеры будут зарегистрированы в том же порядке, в котором они были импортированы
labelers = [chat_labeler, labeler]
__all__ = ("labelers")
