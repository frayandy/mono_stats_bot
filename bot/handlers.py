from aiogram import Dispatcher, types

from bot.bot import bot

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def init_bot(message: types.Message) -> None:
    await message.reply('Echo')


@dp.message_handler(commands=['add_user'])
async def add_user_handler(message: types.Message) -> None:
    await message.reply('User is added')
