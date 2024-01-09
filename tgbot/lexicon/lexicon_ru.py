import asyncio, json

from tgbot.config import load_config
from infrastructure.database.setup import create_engine
from infrastructure.database.setup import create_session_pool
from infrastructure.database.repo.lexicon_ru import LexiconRepo
from infrastructure.database.models import Lexicon_Ru, Lexicon_KB, Lexicon_Admin



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

EVENTS = {
}

with open('events.json', 'r', encoding='utf-8') as f:
        file_contents = f.read()
        events = json.loads(file_contents)
        EVENTS = events        

"""
EVENTS = {
    'event_1': {
        'event_name': 'Мероприятие 1',
        'event_desc': 'Описание мероприятия 1',
        'event_date': '21.11.2023',
        'event_url': 'https://vk.com',
        'event_photo': ['AgACAgIAAxkBAAILTWWdasB0NjlpQ0NHxc2ttcOAXU5wAALY0zEb4YjpSCpRr01zt-1JAQADAgADeQADNAQ', 'AgACAgIAAxkBAAILUGWdasDqUY9fXKSS2tJiS96ynOXtAALd0zEb4YjpSOuuPolRlRxlAQADAgADeQADNAQ', 'AgACAgIAAxkBAAILUWWdasBjEe6r7bOClDu6-wPdVqHyAALe0zEb4YjpSOHCemNb3AAB6gEAAwIAA3kAAzQE', 'AgACAgIAAxkBAAILTmWdasBwFP2FRW5o0RHj5tDpNeZMAALZ0zEb4YjpSGTyDHbj3o0DAQADAgADeQADNAQ', 'AgACAgIAAxkBAAILT2WdasA58230iUh-99J_tJmhTJ24AALa0zEb4YjpSHC1W4rJ7GaAAQADAgADeQADNAQ']
    },
    'event_2': {
        'event_name': 'Мероприятие 2',
        'event_desc': 'Описание мероприятия 2',
        'event_date': '16.12.2024',
        'event_url': 'https://vk.com',
        'event_photo': ['AgACAgIAAxkBAAILUGWdasDqUY9fXKSS2tJiS96ynOXtAALd0zEb4YjpSOuuPolRlRxlAQADAgADeQADNAQ', 'AgACAgIAAxkBAAILTWWdasB0NjlpQ0NHxc2ttcOAXU5wAALY0zEb4YjpSCpRr01zt-1JAQADAgADeQADNAQ', 'AgACAgIAAxkBAAILUWWdasBjEe6r7bOClDu6-wPdVqHyAALe0zEb4YjpSOHCemNb3AAB6gEAAwIAA3kAAzQE', 'AgACAgIAAxkBAAILTmWdasBwFP2FRW5o0RHj5tDpNeZMAALZ0zEb4YjpSGTyDHbj3o0DAQADAgADeQADNAQ', 'AgACAgIAAxkBAAILT2WdasA58230iUh-99J_tJmhTJ24AALa0zEb4YjpSHC1W4rJ7GaAAQADAgADeQADNAQ']
    },
    'event_3': {
        'event_name': 'Мероприятие 3',
        'event_desc': 'Описание мероприятия 3',
        'event_date': '29.12.2024',
        'event_url': 'https://vk.com',
        'event_photo': ['AgACAgIAAxkBAAILTmWdasBwFP2FRW5o0RHj5tDpNeZMAALZ0zEb4YjpSGTyDHbj3o0DAQADAgADeQADNAQ', 'AgACAgIAAxkBAAILT2WdasA58230iUh-99J_tJmhTJ24AALa0zEb4YjpSHC1W4rJ7GaAAQADAgADeQADNAQ']
    },
    'event_4': {
        'event_name': 'Мероприятие 4',
        'event_desc': 'Описание мероприятия 4',
        'event_date': '31.12.2024',
        'event_url': 'https://vk.com',
        'event_photo': ['AgACAgIAAxkBAAILT2WdasA58230iUh-99J_tJmhTJ24AALa0zEb4YjpSHC1W4rJ7GaAAQADAgADeQADNAQ']
    }
}"""


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
asyncio.run(initialize_lexicon_dict(lexicon_ru_dict, Lexicon_Ru))
asyncio.run(initialize_lexicon_dict(lexicon_reply_kb, Lexicon_KB))
asyncio.run(initialize_lexicon_dict(lexicon_admin, Lexicon_Admin))
