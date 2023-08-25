import asyncio
from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from tgbot.misc.states import CollectInfoEss
from tgbot.keyboards.inline import stars
from tgbot.services.ai_analyzer import analyzes


async def result_handler(callback_query: CallbackQuery, state: FSMContext):
    # delete previous message
    await callback_query.message.delete()
    # give to AI to analyze and wait in wait-list
    sticker = "CAACAgIAAxkBAAEKAtlk2RjajYG3KYL6jRVh2Dg0z6srlwACihYAAqe_qEl5G6cHKF2I9zAE"
    stick_wait = await callback_query.message.answer_sticker(sticker=sticker)
    wait = await callback_query.message.answer(text="Wait a minute.. AI analyzes your essay..")
    # get data
    data = await state.get_data()
    info: dict = {"type": data.get('type'),
                  "topic": data.get('topic'),
                  "essay": data.get('essay')}
    # return result
    new_task = asyncio.create_task(analyzes(info['type'], info['topic'], info['essay']))
    data_result = await new_task
    # to avoid too long message error
    if len(data_result) >= 4010:
        a = 4008  # minus 2 from limit
        endlist = [". ", "! ", "? ", "\" ", ".\n", "\"\n", "!\n", "?\n", ".\n"]
        while not (data_result[a:a + 2] in endlist):
            a -= 1
        a += 1
        await callback_query.message.answer(text=data_result[:a])
        await callback_query.message.answer(text=data_result[a + 1:])
    else:
        await callback_query.message.answer(text=data_result)
    # clear waiting notification
    await stick_wait.delete()
    await wait.delete()
    # ask feedback
    await callback_query.message.answer(text="Please leave feedback, how was it?", reply_markup=stars)
    await state.finish()


def register_result_handler(dp: Dispatcher):
    dp.register_callback_query_handler(result_handler, text="finish_inline_cb", state=CollectInfoEss.Last_state)
