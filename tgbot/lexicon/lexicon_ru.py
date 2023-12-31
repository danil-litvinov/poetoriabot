import asyncio

from tgbot.config import load_config
from infrastructure.database.setup import create_engine
from infrastructure.database.setup import create_session_pool
from infrastructure.database.repo.lexicon_ru import LexiconRepo
from infrastructure.database.models import Lexicon_ru, Lexicon_KB, Lexicon_Admin



LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЯ эхо-бот для демонстрации работы роутеров!\n\n'
              'Если хотите - можете мне что-нибудь прислать или '
              'отправить команду /help',
    '/start_admin': f'Привет, админ!',
    '/help': 'Я просто отправляю вам копию вашего сообщения',
    'user': 'Привет, обычный!\n\nЯ эхо-бот для демонстрации работы роутеров!',
    'admin_photo': 'Спасибо за фото, админ!',
    'photo': 'Спасибо за фото, польз!',
    'but_event_1': 'Мероприятие 1',
    'but_event_2': 'Мероприятие 2',
    'but_event_3': 'Мероприятие 3',
    'edit_event_button': 'Редактировать',
    'cancel_button': 'Отмена',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
}

LEXICON_ERR: dict[str, str] = {
    'update_dict_err': 'Ошибка с командой /update_dict\n\n'
        'Значение столбца «text_name» должно быть равно «update_dict», проверьте в базе данных\n\n'
        'Код ошибки: {}',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
}

# Создайте функцию для инициализации словаря (эту функцию можно вызвать один раз)
async def initialize_lexicon_dict(target_dict, lexicon_model):
    config = load_config(".env")
    session_factory = create_session_pool(create_engine(config.db))
    lexicon_repo = LexiconRepo(session_factory, lexicon_model)
    await lexicon_repo.read_lexicon_table()
    target_dict.update(lexicon_repo.lexicon_dict)  # Обновите словарь значениями из базы данных

lexicon_ru_dict:dict[str, str] = {}
lexicon_reply_kb:dict[str, str] = {}
lexicon_admin:dict[str, str] = {}

# Вызовите функцию для инициализации словаря при импорте модуля
asyncio.run(initialize_lexicon_dict(lexicon_ru_dict, Lexicon_ru))
asyncio.run(initialize_lexicon_dict(lexicon_reply_kb, Lexicon_KB))
asyncio.run(initialize_lexicon_dict(lexicon_admin, Lexicon_Admin))
