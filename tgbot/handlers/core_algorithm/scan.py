from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from tgbot.misc.states import CollectInfoEss
from tgbot.keyboards.inline import check_scan


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
    photo_url = data.get("photo_url")
    stick_wait = await callback_query.message.answer_sticker(sticker="CAACAgIAAxkBAAEKAtNk2RRMD5jbBuNqtQaH2BvimRZ6BwACJRYAAh9BoEmSDZPG0WhzIjAE")
    wait = await callback_query.message.answer(text="Just a sec.. I'm scaninng..")
    answer = "scanned text"#scanning(photo_url)
    await callback_query.message.answer(text=answer)
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
    await callback_query.message.answer(text=f"`{answer}`\n\n\nCopy text and rewrite correcting scanner errors:",
                                        parse_mode="MARKDOWN")
    await CollectInfoEss.next()


def register_scan(dp: Dispatcher):
    dp.register_callback_query_handler(scan_photo, state=CollectInfoEss.Scan_Topic_state, text="next_photo_inline_cbT")
    dp.register_callback_query_handler(scan_photo, state=CollectInfoEss.Scan_Essay_state, text="next_photo_inline_cbE")
    dp.register_callback_query_handler(check_scan_no, state=CollectInfoEss.Scan_Topic_state, text="no_inline_cb")
    dp.register_callback_query_handler(check_scan_no, state=CollectInfoEss.Scan_Essay_state, text="no_inline_cb")
