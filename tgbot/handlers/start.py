from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from tgbot.keyboards.reply import menu
from tgbot.misc.states import CollectInfoEss


async def start_user(message: Message, state: FSMContext):
    await state.reset_state()  # RESET STATES
    # QUESTION FOR TYPE_ESSAY
    await message.answer(text="<b>Let\'s start analyzing your essay! 🔍</b>"
                              "\nFirst, I need to gather data about the essay such as these:\n"
                              "\n📌 <b>Type of essay</b>"
                              "\n❔ <b>The question of the essay</b>"
                              "\n📜 <b>The essay</b> ")

    await message.answer(text="<b>Choose what TYPE OF ESSAY you have:</b>", reply_markup=menu)
    # await message.answer(text="You will be provided with IETLS writing task 2. Your task is conduct a thorough analysis of the presented essay in line with the evaluation criteria of IELTS Writing Task 2. For each of the four specified criteria: **Task Achievement**, **Coherence and Cohesion**, **Lexical Resource**, and **Grammatical Range and Accuracy**, provide a score from 0 to 9 and justify it with examples from the text. Additionally, highlight the strengths of the work and provide constructive feedback on potential areas for improvement.\n\nPattern:\n\n**Feedback:**\n- **Task Achievement:** Score: X with float. Example: Your response doesn't fully cover all aspects of the topic. For instance, in point Y, you could have included more in-depth arguments.\n- **Coherence and Cohesion:** Score: X with float. Example: Your text is easily readable, but the paragraph structure in point Z could be more consistent.\n- **Lexical Resource:** Score: X with float. Example: Your vocabulary is impressive; however, using specific terms in point W could enhance your argumentation.\n- **Grammatical Range and Accuracy:** Score: X with float. Example: Your grammar is generally good, but in sentence V, pay attention to the correct use of tenses.(Underlined error: \"needs\" should be \"need\".)\n\n**Overall:**Score: X with float. Example: Your score is that because..\n\n**Strengths:**\nCompelling arguments in point A, a good flow of ideas in point B.\n\n**Areas for Improvement:**\nDeeper analysis in point C, maintaining consistency in point D.\n\nPlease use this analysis to further develop your writing skills.\n\nThank you for your work on the essay!")
    await CollectInfoEss.Type_essay_state.set()


async def get_url_video(message: Message):
    video = message.video.file_id
    await message.answer(text=video)


def register_start_user(dp: Dispatcher):
    dp.register_message_handler(get_url_video, content_types='video', state="*")
    dp.register_message_handler(start_user, commands="start")
    dp.register_message_handler(start_user, text="🔙 Back")
    dp.register_message_handler(start_user, commands="start", state="*")
    dp.register_message_handler(start_user, text="🔙 Back", state=CollectInfoEss.Topic_state)
