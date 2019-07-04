from aiogram import Bot

from bot.config import BotConfig

config = BotConfig()
bot = Bot(token=config.token)
