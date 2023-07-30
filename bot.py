import asyncio
import logging

from aiogram import Bot, Dispatcher

from tgbot.config import load_config, Config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.echo import register_echo
from tgbot.handlers.admin import register_admin

logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_echo(dp)
    register_admin(dp)


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("starting bot")
    config: Config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot)

    bot['config'] = config
    register_all_handlers(dp)
    # start
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
        logger.error("bot stopped!")
