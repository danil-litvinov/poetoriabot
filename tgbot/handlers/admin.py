import asyncio

from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from tgbot.lexicon.lexicon_ru import LEXICON_ERR, lexicon_ru_dict, lexicon_main_menu_ru, lexicon_reply_kb, lexicon_admin, initialize_lexicon_dict

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(Command(commands='update_dict'))
async def update_lexicon_command(message: Message):
    await initialize_lexicon_dict(lexicon_ru_dict)
    await initialize_lexicon_dict(lexicon_main_menu_ru)
    await initialize_lexicon_dict(lexicon_reply_kb)
    await initialize_lexicon_dict(lexicon_admin)
    try:
        await message.reply(text=lexicon_admin['update_dict'])
    except Exception as e:
        await message.reply(LEXICON_ERR['update_dict_err'].format(e))

@admin_router.message(F.photo)
async def admin_start(message: Message):
    await message.answer_photo(message.photo[0].file_id)

