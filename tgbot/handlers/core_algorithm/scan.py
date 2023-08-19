import asyncio
import re

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline import check_scan
from tgbot.misc.states import CollectInfoEss
from tgbot.services.scaner import scanning


# to detect which photo need to scan
def find_state_data(current_state):
    if current_state == "CollectInfoEss:Scan_Topic_state":
        return "topic"
    elif current_state == "CollectInfoEss:Scan_Essay_state":
        return "essay"
    else:
        return "you are not in state."


async def scan_photo(callback_query: CallbackQuery, state: FSMContext):
    # Analyze answer photo
    await callback_query.message.delete()
    data = await state.get_data()
    photo_url: str = data.get("photo_url")
    sticker = "CAACAgIAAxkBAAEKAtNk2RRMD5jbBuNqtQaH2BvimRZ6BwACJRYAAh9BoEmSDZPG0WhzIjAE"
    stick_wait = await callback_query.message.answer_sticker(
        sticker=sticker)
    wait = await callback_query.message.answer(text="Just a sec.. I'm scaninng..")




    # getting result
    data_task = asyncio.create_task(scanning(photo_url))
    answer: str = await data_task



    answer: str = re.sub(pattern=r'(?<!\.)\n', repl=' ', string=answer)
    answer: str = re.sub(pattern=r'\n', repl='\n\n', string=answer)
    answer: str = re.sub(pattern=r' +', repl=' ', string=answer)

    await callback_query.message.answer(text=answer)
    # clear waiting messages
    await stick_wait.delete()
    await wait.delete()

    # to save answer as topic or essay
    current_state = await state.get_state()
    async with state.proxy() as data:
        data[find_state_data(current_state)] = answer
    # question to be proud
    await callback_query.message.answer(text="text scanned correctly?", reply_markup=check_scan)


async def check_scan_no(callback_query: CallbackQuery, state: FSMContext):
    # rewrite and correct answer
    await callback_query.message.delete()
    data = await state.get_data()
    current_state = await state.get_state()
    answer = data.get(find_state_data(current_state))
    await callback_query.message.answer(text=f"`{answer}`\n\n\n💾 Copy text and rewrite correcting scanner errors:",
                                        parse_mode="MARKDOWN")
    await CollectInfoEss.next()


def register_scan(dp: Dispatcher):
    dp.register_callback_query_handler(scan_photo, state=CollectInfoEss.Scan_Topic_state, text="next_photo_inline_cbT")
    dp.register_callback_query_handler(scan_photo, state=CollectInfoEss.Scan_Essay_state, text="next_photo_inline_cbE")
    dp.register_callback_query_handler(check_scan_no, state=CollectInfoEss.Scan_Topic_state, text="no_inline_cb")
    dp.register_callback_query_handler(check_scan_no, state=CollectInfoEss.Scan_Essay_state, text="no_inline_cb")
