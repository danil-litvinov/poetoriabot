from aiogram import Router
from aiogram.types import Message

from tgbot.lexicon.lexicon_ru import lexicon_ru_dict

router = Router()

# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=lexicon_ru_dict['other_answer'])

