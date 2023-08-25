from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from tgbot.keyboards.inline import scan_ess, check_text_top, check_photo_top
from tgbot.misc.states import CollectInfoEss


async def scan_inline_topic(callback_query: CallbackQuery):
    # analyze callback scan
    await callback_query.message.answer_video(
        video="BAACAgIAAxkBAAIYXWTZB8eebfgI82hc_9BNGkcYnGxOAALvMwAC1lzISuM8j32ADkzUMAQ",
        caption='⬆️<b> Illustration </b>⬆️'
                '\nSubmit your <i>QUESTION</i> according to these rules!\n\n'
                '<b>📋Rules:'
                "\n• <u>One photo - one QUESTION</u>"
                "\n• <u>The photo should be vertical</u>"
                "\n• <u>Only the QIESTION should be on the photo, no other texts</u>"
                "\n• <u>Photo quality should be normal and readable\n\n</u></b>"         
                "<b>💡Advice:</b>"
                "\n•<i> Without any strikethrough text</i>",
        reply_markup=ReplyKeyboardRemove())
    # delete previous callback
    await callback_query.message.delete()
    # next state
    await CollectInfoEss.Scan_Topic_state.set()


async def scan_photo_topic(message: Message, state: FSMContext):
    # get photo and save
    photo = message.photo[-1]
    photo_url = await photo.get_url()
    async with state.proxy() as data:
        data["photo_url"] = photo_url
    # to be sure
    await message.answer_photo(message.photo[-1].file_id,
                               caption="Ensure the photo follows these rules:"
                                       "\n1. Vertical orientation."
                                       "\n2. Only the question text on the photo."
                                       "\n3. Clear and readable quality."
                                       "\n\n<b>Click next to continue or resend photo:</b>",
                               reply_markup=check_photo_top)


async def continue_topic(message: Message, state: FSMContext):
    if len(message.text) >= 4:
        # analyze answer topic essay and save
        answer = message.text
        async with state.proxy() as data:
            data["topic"] = answer
        # to be sure
        await message.answer(text=f"<b>Your entered  Question:</b>\n\"<i>{answer}</i>\"\n\n"
                                  "<b>Click next to continue or resend text:</b>",
                             reply_markup=check_text_top)
        await CollectInfoEss.Topic_state.set()
    else:
        await message.answer(text="It's not a Question. Resend again.")


async def essay_topic_handler(callback_query: CallbackQuery, state: FSMContext):
    # get data
    data = await state.get_data()
    topic = data.get('topic')
    # delete callbacks
    await callback_query.message.delete()
    await callback_query.message.answer(
        text=f"<b>You've entered question successfully!\n\nQuestion:\n</b> \"<i>{topic}</i>\"",
        reply_markup=ReplyKeyboardRemove())
    # question for essay body
    await callback_query.message.answer_video(
        video="BAACAgIAAxkBAAIWNWTYxsY2-z8sJNfqL1fpTNMsl81GAAIqMQAC1lzISj6BdA60x97sMAQ",
        caption='⬆️<b> Illustration </b>⬆️\n'
                "<b>Now, please provide your <i>ESSAY</i></b>:\n\n"
                "We offer two text upload options:\n<i>• Paste the text\n• Scan text from a photo</i>\n\n"
                '<b>Enter your text:</b>',
        reply_markup=scan_ess)
    # next state
    await CollectInfoEss.Essay_state.set()


# register all cbs and handlers
def register_essay_topic(dp: Dispatcher):
    dp.register_callback_query_handler(scan_inline_topic, state=CollectInfoEss.Scan_Topic_state, text="againT")
    dp.register_callback_query_handler(scan_inline_topic, state=CollectInfoEss.Topic_state, text="scan_inline_cbT")
    dp.register_message_handler(continue_topic, state=CollectInfoEss.Topic_state)
    dp.register_message_handler(continue_topic, state=CollectInfoEss.next_text_topic_state)
    dp.register_message_handler(scan_photo_topic, state=CollectInfoEss.Scan_Topic_state, content_types="photo")

    dp.register_callback_query_handler(essay_topic_handler, text="next_inline_cbT", state=CollectInfoEss.Topic_state)
    dp.register_callback_query_handler(essay_topic_handler, state=CollectInfoEss.Scan_Topic_state, text="yes_inline_cb")
