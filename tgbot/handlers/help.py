from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove
from tgbot.misc.states import CollectInfoEss


async def instruction_handler(message: Message):
    await message.answer("DO NOT BE SO STUPID!", reply_markup=ReplyKeyboardRemove())


def register_instruction_handler(dp: Dispatcher):
    dp.register_message_handler(instruction_handler, commands="help", state=CollectInfoEss.Type_essay_state)
    dp.register_message_handler(instruction_handler, commands="help")
