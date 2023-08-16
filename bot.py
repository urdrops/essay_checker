import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
# cycle of polling
from tgbot.handlers.start import register_start_user
from tgbot import register_start_collect
from tgbot import register_essay_topic
from tgbot import register_essay
from tgbot import register_scan
from tgbot import register_error_handler
from tgbot import register_get_feedback
from tgbot import register_result_handler
# commands
from tgbot import register_instruction_handler


logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    pass


def register_all_filters(dp):
    pass


def register_all_handlers(dp):
    # commands
    register_start_user(dp)
    register_instruction_handler(dp)
    # polls
    register_start_collect(dp)
    register_essay_topic(dp)
    register_essay(dp)
    register_scan(dp)
    register_result_handler(dp)
    # last priority
    register_get_feedback(dp)
    register_error_handler(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
