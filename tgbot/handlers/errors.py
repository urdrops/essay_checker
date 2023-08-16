from aiogram import Dispatcher
from aiogram.types import Message, Update
import logging


async def errors_handler(update: Update, exception: Exception):
    from aiogram.utils import (Unauthorized, InvalidQueryID, TelegramAPIError,
                               MessageNotModified, MessageToDeleteNotFound,
                               MessageTextIsEmpty,
                               RetryAfter, CantParseEntities,
                               MessageCantBeDeleted, BadRequest)
    if isinstance(exception, Unauthorized):
        updt = update.get_current()
        logging.debug(f"error: Unauthorized \n{updt}")
        return True
    if isinstance(exception, CantParseEntities):
        updt = update.get_current()
        logging.debug(f"error: CantParseEntities\n{updt}")
        return True
    if isinstance(exception, InvalidQueryID):
        updt = update.get_current()
        logging.debug(f"error: InvalidQueryID\n{updt}")
        return True
    if isinstance(exception, TelegramAPIError):
        logging.debug(f"error: TelegramAPIError")
        return True
    if isinstance(exception, MessageNotModified):
        logging.debug(f"error: MessageNotModified")
        return True
    if isinstance(exception, MessageToDeleteNotFound):
        logging.debug(f"error: MessageToDeleteNotFound")
        return True
    if isinstance(exception, MessageTextIsEmpty):
        logging.debug(f"error: MessageTextIsEmpty")
        return True
    if isinstance(exception, RetryAfter):
        logging.debug(f"error: RetryAfter")
        return True
    if isinstance(exception, MessageCantBeDeleted):
        updt = update.get_current()
        logging.debug(f"error: MessageCantBeDeleted\n{updt}")
        return True
    if isinstance(exception, BadRequest):
        updt = update.get_current()
        logging.debug(f"error: BadRequest\n{updt}")
        return True


# if no handlers
async def error_handler(message: Message):
    await message.answer(text="There's no such option")


def register_error_handler(dp: Dispatcher):
    dp.register_message_handler(error_handler, state="*", content_types="text")
    dp.register_message_handler(error_handler, state="*", content_types="photo")
    dp.register_message_handler(error_handler, state="*", content_types="animation")
    dp.register_message_handler(errors_handler)

