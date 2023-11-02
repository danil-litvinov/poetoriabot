from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from tgbot.lexicon.lexicon_ru import lexicon_ru_dict, lexicon_reply_kb
from tgbot.keyboards.reply.start_kb import create_reply_kb



user_router = Router()



@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(text=lexicon_ru_dict['/start'], reply_markup=create_reply_kb(1, 'contact_us', 'donate'))

# Этот хэндлер срабатывает на команду /help
@user_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=lexicon_ru_dict['/help'], reply_markup=create_reply_kb(1, 'contact_us', 'back'))

@user_router.message(F.text == lexicon_reply_kb['donate'])
async def process_donate_answer(message: Message):
    await message.answer(text=lexicon_ru_dict['donate'], reply_markup=create_reply_kb(1, 'back'))

@user_router.message(F.text == lexicon_reply_kb['contact_us'])
async def process_donate_answer(message: Message):
    await message.answer(text=lexicon_ru_dict['contact_us'], reply_markup=create_reply_kb(1, 'back'))

@user_router.message(F.text == lexicon_reply_kb['back'])
async def process_donate_answer(message: Message):
    await message.answer(text=lexicon_ru_dict['/start'], reply_markup=create_reply_kb(1, 'contact_us', 'donate'))

@user_router.message(F.photo)
async def admin_start(message: Message):
    await message.answer(lexicon_ru_dict['photo'])
