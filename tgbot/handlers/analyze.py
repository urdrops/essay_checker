import asyncio
import time

from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from tgbot.keyboards.reply import menu
from tgbot.misc.states import CollectInfoEss


async def start_user(message: Message, state: FSMContext):
    await state.reset_state()  # RESET STATES
    # QUESTION FOR TYPE_ESSAY
    await message.answer(text="<b>Let\'s start analyzing your essay! 🔍</b>"
                              "\nFirst, I'll gather data about the essay such as:\n"
                              "\n📌 <b>The type of exam</b>"
                              "\n❔ <b>The topic or question of the essay</b>"
                              "\n📜 <b>The content of the essay</b> ")
    await message.answer(text="<b>Please indicate the EXAM TYPE of your essay:</b>", reply_markup=menu)
    await CollectInfoEss.Type_essay_state.set()


async def get_url_video(message: Message):
    video = message.video.file_id
    await message.answer(text=video)


def register_start_user(dp: Dispatcher):
    dp.register_message_handler(get_url_video, content_types='video', state="*")
    dp.register_message_handler(start_user, commands="analyze")
    dp.register_message_handler(start_user, text="🔙 Back")
    dp.register_message_handler(start_user, commands="analyze", state="*")
    dp.register_message_handler(start_user, text="🔙 Back", state=CollectInfoEss.Topic_state)
