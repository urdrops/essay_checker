from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher import FSMContext
from tgbot.misc.states import CollectInfoEss
from tgbot.keyboards.inline import check_text_ess, check_photo_ess, finish_inline


async def scan_inline_essay(callback_query: CallbackQuery):
    # analyze callback scan
    await callback_query.message.answer_video(
        video="BAACAgIAAxkBAAIYXWTZB8eebfgI82hc_9BNGkcYnGxOAALvMwAC1lzISuM8j32ADkzUMAQ",
        caption='⬆️<b> Example </b>⬆️'
                '\n<b>Submit your <i>ESSAY</i> following these rules!</b>\n\n'
                '<b>📋Rules:\n</b>'
                "\n• Your essay must be completely on one photo, the bot scans only 1 photo❗️"
                "\n• Make sure that there are no other texts on the photo except for the essay❗️"
                "\n• Your photo must be vertical❗️"
                "\n• Make sure the quality of the photo is normal and readable❗️\n\n"


                "<b>💡Advice:</b>\n"
                "\n• Preferably your essay should be clean and on a white sheet"
                "\n• Without any strikethrough text",
        reply_markup=ReplyKeyboardRemove())
    await callback_query.message.delete()
    # next state
    await CollectInfoEss.Scan_Essay_state.set()


async def scan_photo_essay(message: Message, state: FSMContext):
    # analyze and save photo to scan
    photo = message.photo[-1]
    photo_url = await photo.get_url()
    async with state.proxy() as data:
        data["photo_url"] = photo_url
    # to be sure
    await message.answer_photo(message.photo[-1].file_id,
                               caption="[your input photo]\n\n<b>Click next to continue or resend photo:</b>",
                               reply_markup=check_photo_ess)



async def continue_essay(message: Message, state: FSMContext):
    # analyze answer essay body
    answer = message.text
    async with state.proxy() as data:
        data["essay"] = answer
    # to be sure
    await message.answer(text=f"<b>Your entered  Essay:</b>\n\n\"<i>{answer}</i>\"\n\n"
                              "<b>Click next to continue or resend text:</b>", reply_markup=check_text_ess)
    # next state
    await CollectInfoEss.Essay_state.set()


async def essay_body_handler(callback_query: CallbackQuery, state: FSMContext):
    # delete previous message
    await callback_query.message.delete()
    # get data
    data = await state.get_data()
    type1 = data.get('type')
    topic = data.get('topic')
    essay = data.get('essay')
    # answer
    await callback_query.message.answer(text=f'<b>✅You\'ve finished polls successfully!</b>',
                                        reply_markup=ReplyKeyboardRemove())
    await callback_query.message.answer(text=f"<b>📌 Type:</b> \"<i>{type1}</i>\"\n"
                                        f"\n<b>❔ Question:</b> \"<i>{topic}</i>\"\n"
                                        f"\n<b>📜 Essay:</b> \"<i>{essay}</i>\"\n",
                                        reply_markup=finish_inline)
    await CollectInfoEss.Last_state.set()


# register all callbacks and handlers
def register_essay(dp: Dispatcher):
    dp.register_callback_query_handler(scan_inline_essay, state=CollectInfoEss.Essay_state, text='scan_inline_cbE')
    dp.register_callback_query_handler(scan_inline_essay, state=CollectInfoEss.Scan_Essay_state, text='againE')
    dp.register_message_handler(scan_photo_essay, state=CollectInfoEss.Scan_Essay_state, content_types="photo")
    dp.register_message_handler(continue_essay, state=CollectInfoEss.Essay_state)
    dp.register_message_handler(continue_essay, state=CollectInfoEss.next_text_essay_state)
    dp.register_callback_query_handler(essay_body_handler, state=CollectInfoEss.Essay_state, text="next_inline_cbE")
    dp.register_callback_query_handler(essay_body_handler, state=CollectInfoEss.Scan_Essay_state, text="yes_inline_cb")
