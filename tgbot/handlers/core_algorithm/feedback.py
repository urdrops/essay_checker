from aiogram import Dispatcher
from aiogram.types import CallbackQuery


# last messages after feedback
async def get_feedback(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer(text='Thanks for the feedback!' 
                                             '\nClick [/analyze] to analyze more!')


# register feedback
def register_get_feedback(dp: Dispatcher):
    dp.register_callback_query_handler(get_feedback, text='1')
    dp.register_callback_query_handler(get_feedback, text='2')
    dp.register_callback_query_handler(get_feedback, text='3')
    dp.register_callback_query_handler(get_feedback, text='4')
    dp.register_callback_query_handler(get_feedback, text='5')
