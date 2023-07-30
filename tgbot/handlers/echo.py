from aiogram import types, Dispatcher


async def bot_echo(message: types.Message):
    await message.answer("bot works")


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
