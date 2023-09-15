import asyncio
import asyncpg
import logging

from tgbot.config import DbConfig


async def create_db():
    create_db_command = open("create_db.sql", "r").read()
    conn: asyncpg.Connection = await asyncpg.connect(user=DbConfig.user,
                                                     password=DbConfig.password,
                                                     host=DbConfig.host)
    await conn.execute(create_db_command)
    logging.info("table has been created")
    await conn.close()


async def create_pool():
    return await asyncpg.create_pool(
        user=DbConfig.user,
        password=DbConfig.password,
        host=DbConfig.host
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
