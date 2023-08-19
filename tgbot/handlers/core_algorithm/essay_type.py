from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from tgbot.keyboards.reply import back
from tgbot.keyboards.inline import scan_top
from tgbot.misc.states import CollectInfoEss


async def essay_type_handler(message: Message, state: FSMContext):
    # analyze answer essay type and save
    answer = message.text
    async with state.proxy() as data:
        data["type"] = answer
    # show answer and question for next
    await message.answer(text=f"<b>All right!✅ \nYou've chosen <u><i>{answer}</i></u></b>!\n",
                         reply_markup=back)

    # question for topic essay
    await message.answer_video(video="BAACAgIAAxkBAAIWNWTYxsY2-z8sJNfqL1fpTNMsl81GAAIqMQAC1lzISj6BdA60x97sMAQ",
                               caption="⬆<b> Illustration </b>⬆\n"
                                       'Now, please provide <b>the QUESTION</b> of your writing essay.\n\n'
                                       "We offer two text upload options:\n"
                                       "<i>• Paste the text\n• Scan text from a photo</i>"
                                       '\n\n<b>Enter your text:</b>',
                               reply_markup=scan_top)
    await CollectInfoEss.Topic_state.set()


async def motiv_handler(message: Message, state: FSMContext):
    # analyze answer motiv letter
    await message.answer(text='Coming soon..', reply_markup=back)
    # end state
    await state.finish()


def register_start_collect(dp: Dispatcher):
    dp.register_message_handler(essay_type_handler, text="IELTS (writing task 2)",
                                state=CollectInfoEss.Type_essay_state)
    dp.register_message_handler(essay_type_handler, text="TOEFL (writing task)", state=CollectInfoEss.Type_essay_state)
    dp.register_message_handler(essay_type_handler, text="Essays | CEFR", state=CollectInfoEss.Type_essay_state)
    dp.register_message_handler(motiv_handler, text="Motivation letter", state=CollectInfoEss.Type_essay_state)
