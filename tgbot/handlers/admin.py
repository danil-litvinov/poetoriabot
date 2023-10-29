import asyncio

from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
#from tgbot.lexicon.lexicon_ru import LEXICON_RU
from tgbot.keyboards.inline.event_kb import create_event_kb
from tgbot.lexicon.lexicon_ru import lexicon_ru_dict, initialize_lexicon_dict, LEXICON_ERR

admin_router = Router()
admin_router.message.filter(AdminFilter())

@admin_router.message(CommandStart())
async def admin_start(message: Message):

    # Используйте ключи для создания клавиатуры
    keyboard = create_event_kb(2, lexicon_ru_dict['start'], lexicon_ru_dict['start'], lexicon_ru_dict['start'], lexicon_ru_dict['edit_event_button'], lexicon_ru_dict['cancel_button'])

    await message.reply(lexicon_ru_dict['start'], reply_markup=keyboard)

@admin_router.message(Command(commands='update_dict'))
async def update_lexicon_command(message: Message):
    await initialize_lexicon_dict(lexicon_ru_dict)
    try:
        await message.reply(lexicon_ru_dict['update_dict'])
    except Exception as e:
        await message.reply(LEXICON_ERR['update_dict_err'].format(e))

@admin_router.message(F.photo)
async def admin_start(message: Message):
    await message.answer_photo(message.photo[0].file_id)

