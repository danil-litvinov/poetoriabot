import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder

from tgbot.config import load_config, Config
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.middlewares.database import DatabaseMiddleware
from tgbot.handlers import routers_list
from tgbot.services import broadcaster
from infrastructure.database.setup import create_engine
from infrastructure.database.setup import create_session_pool



async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Бот запущен /start")


def register_global_middlewares(dp: Dispatcher, config: Config):
    """
    Register global middlewares for the given dispatcher.
    Global middlewares here are the ones that are applied to all the handlers (you specify the type of update)

    :param dp: The dispatcher instance.
    :type dp: Dispatcher
    :param config: The configuration object from the loaded configuration.
    :param session_pool: Optional session pool object for the database using SQLAlchemy.
    :return: None
    """

    db_config = config.db

    engine = create_engine(db_config)
    session_pool = create_session_pool(engine)

    middleware_types = [
        ConfigMiddleware(config),
        DatabaseMiddleware(session_pool),
    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)


def setup_logging():
    """
    Set up logging configuration for the application.

    This method initializes the logging configuration for the application.
    It sets the log level to INFO and configures a basic colorized log for
    output. The log format includes the filename, line number, log level,
    timestamp, logger name, and log message.

    Returns:
        None

    Example usage:
        setup_logging()
    """
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


def get_storage(config):
    """
    Return storage based on the provided configuration.

    Args:
        config (Config): The configuration object.

    Returns:
        Storage: The storage object based on the configuration.

    """
    if config.tg_bot.use_redis:
        return RedisStorage.from_url(
            config.redis.dsn(),
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )
    else:
        return MemoryStorage()

'''async def read_lexicon_table(self):
    async with self.session_factory() as session:
        # Читаем таблицу 'lexicon'
        lexicon_data = (await session.execute(select(Lexicon))).scalars().all()

        # Генерируем словарь
        self.lexicon_dict = {item.text_name: item.content for item in lexicon_data}'''

async def main():
    setup_logging()

    config = load_config(".env")
    storage = get_storage(config)

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=storage)

    #await set_main_menu(bot)

    dp.include_routers(*routers_list)

    register_global_middlewares(dp, config)

    '''session_factory = create_session_pool(create_engine(config.db))  # Создать session_factory

    # Создайте экземпляр LexiconRepo и передайте session_factory
    lexicon_repo = LexiconRepo(session_factory)

    # Вызовите метод read_lexicon_table на экземпляре класса
    await lexicon_repo.read_lexicon_table()

    # Получите словарь lexicon_dict
    lexicon_dict = lexicon_repo.lexicon_dict

    # Выведите словарь на печать
    for key, value in lexicon_dict.items():
        print(f"Ключ: {key}, Значение: {value}")'''

    await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот остановлен")
