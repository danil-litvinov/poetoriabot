from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from tgbot.filters.admin import AdminFilter
from tgbot.lexicon.lexicon_ru import lexicon_ru_dict, lexicon_reply_kb, lexicon_admin, initialize_lexicon_dict, EVENTS
from infrastructure.database.models import Lexicon_Ru, Lexicon_KB, Lexicon_Admin
from tgbot.keyboards.reply.start_kb import create_reply_kb
from tgbot.keyboards.inline.event_kb import create_events_kb


admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(Command(commands='update_dict'))
async def update_lexicon_command(message: Message):
    await initialize_lexicon_dict(lexicon_reply_kb, Lexicon_KB)
    await initialize_lexicon_dict(lexicon_ru_dict, Lexicon_Ru)
    await initialize_lexicon_dict(lexicon_admin, Lexicon_Admin)
    try:
        await message.reply(text=lexicon_admin['update_dict'])
    except Exception as e:
        await message.reply(text=lexicon_admin['update_dict'])

@admin_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(text=lexicon_ru_dict['/start'], reply_markup=create_reply_kb(1, 'contact_us', 'donate', 'events'))

@admin_router.message(F.text == lexicon_reply_kb['events'])
@admin_router.callback_query(F.data == 'last_btn')
async def process_events(message: Message):
    keyboard = create_events_kb(1, *EVENTS.keys(), back_button=True)
    if isinstance(message, Message):
        await message.answer(text=lexicon_ru_dict['events'], reply_markup=keyboard)
    elif isinstance(message, CallbackQuery):
        callback=message
        await callback.answer()
        await callback.message.edit_text(text=lexicon_ru_dict['events'], reply_markup=keyboard)
    
@admin_router.message(F.text == lexicon_reply_kb['back'] or F.data == 'back')
@admin_router.callback_query(F.data == 'back')
async def process_back_answer(message):
    keyboard=create_reply_kb(1, 'contact_us', 'donate', 'events')
    if isinstance(message, Message):
        await message.answer(text=lexicon_ru_dict['/start'], reply_markup=keyboard)
    elif isinstance(message, CallbackQuery):
        callback=message
        await callback.answer()
        await callback.message.edit_text(text=lexicon_ru_dict['/start'], reply_markup=None)

@admin_router.message(F.photo)
async def admin_start(message: Message):
    await message.answer(text=str(message.photo[-1].file_id))

