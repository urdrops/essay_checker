from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply("wassup my nigga?")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['start'], is_admin=True)
