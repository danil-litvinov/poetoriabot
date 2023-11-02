from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from tgbot.lexicon.lexicon_ru import lexicon_ru_dict, lexicon_reply_kb, lexicon_admin, initialize_lexicon_dict
from infrastructure.database.models import Lexicon_ru, Lexicon_KB, Lexicon_Admin

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(Command(commands='update_dict'))
async def update_lexicon_command(message: Message):
    await initialize_lexicon_dict(lexicon_ru_dict, Lexicon_ru)
    await initialize_lexicon_dict(lexicon_reply_kb, Lexicon_KB)
    await initialize_lexicon_dict(lexicon_admin, Lexicon_Admin)
    try:
        await message.reply(text=lexicon_admin['update_dict'])
    except Exception as e:
        await message.reply(text=lexicon_admin['update_dict'])
    #    await message.reply(LEXICON_ERR['update_dict_err'].format(e))

@admin_router.message(F.photo)
async def admin_start(message: Message):
    await message.answer_photo(message.photo[0].file_id)

