from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from tgbot.misc.states import CollectInfoEss
from tgbot.keyboards.inline import stars


async def result_handler(callback_query: CallbackQuery, state: FSMContext):
    # delete previous message
    await callback_query.message.delete()
    # give to AI to analyze and wait in wait-list
    stick_wait = await callback_query.message.answer_sticker(sticker="CAACAgIAAxkBAAEKAtlk2RjajYG3KYL6jRVh2Dg0z6srlwACihYAAqe_qEl5G6cHKF2I9zAE")
    wait = await callback_query.message.answer(text="Wait a minute.. AI analyzes your essay..")
    # get data
    data = await state.get_data()
    type1 = data.get('type')
    topic = data.get('topic')
    essay = data.get('essay')
    # return result
    await callback_query.message.answer(text=f"answer")#{analyzes(type1, topic, essay)}
    await stick_wait.delete()
    await wait.delete()
    # ask feedback
    await callback_query.message.answer(text="Please leave feedback, how was it?", reply_markup=stars)
    await state.finish()


def register_result_handler(dp: Dispatcher):
    dp.register_callback_query_handler(result_handler, text="finish_inline_cb", state=CollectInfoEss.Last_state)
