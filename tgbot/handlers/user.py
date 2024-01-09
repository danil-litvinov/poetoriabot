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
async def process_back_answer(message):
    keyboard=create_reply_kb(1, 'contact_us', 'donate')
    await message.answer(text=lexicon_ru_dict['/start'], reply_markup=keyboard)

'''@user_router.message(F.text == lexicon_reply_kb['events'])
@user_router.callback_query(F.data == 'last_btn')
async def process_events(message: Message):
    keyboard = create_events_kb(1, *EVENTS.keys(), back_button=True)
    if isinstance(message, Message):
        await message.answer(text="Список мероприятий:", reply_markup=keyboard)
    elif isinstance(message, CallbackQuery):
        callback=message
        await callback.answer()
        await callback.message.edit_text(text='Список мероприятий:', reply_markup=keyboard)
    
@user_router.message(F.text == lexicon_reply_kb['back'] or F.data == 'back')
@user_router.callback_query(F.data == 'back')
async def process_back_answer(message):
    keyboard=create_reply_kb(1, 'contact_us', 'donate', 'events')
    if isinstance(message, Message):
        await message.answer(text=lexicon_ru_dict['/start'], reply_markup=keyboard)
    elif isinstance(message, CallbackQuery):
        callback=message
        await message.answer()
        #await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.message.edit_text(text=lexicon_ru_dict['/start'], reply_markup=None)'''
