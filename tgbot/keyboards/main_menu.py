from aiogram import Bot
from aiogram.types import BotCommand

from tgbot.lexicon.lexicon_ru import lexicon_main_menu_ru


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command,
        description in lexicon_main_menu_ru.items()]
    await bot.set_my_commands(main_menu_commands)