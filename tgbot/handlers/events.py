from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from datetime import datetime

from tgbot.keyboards.inline.event_kb import create_inline_kb
from tgbot.lexicon.lexicon_ru import EVENTS


events_router = Router()


@events_router.callback_query(F.data.contains('event'))
async def process_back_answer(callback: CallbackQuery):
    await callback.answer()
    event_desc = EVENTS[callback.data]['event_desc']
    photos = EVENTS[callback.data]['event_photo']
    event_date = EVENTS[callback.data]['event_date']
    event_url = EVENTS[callback.data]['event_url']
    event_date_form = datetime.strptime(event_date, "%d.%m.%Y")
    current_date = datetime.now()
    media = [InputMediaPhoto(media=photos[0], caption=event_desc)]
    for photo_id in photos[1:]:
        media.append(InputMediaPhoto(media=photo_id))
    await callback.message.bot.send_media_group(chat_id=callback.message.chat.id, media=media)

    if event_date_form < current_date:
        keyboard = create_inline_kb(1, url=('Скачать фотографии', event_url), last_btn='Назад')
        await callback.message.answer(text='Мероприятие завершено', reply_markup=keyboard)
    elif event_date_form == current_date:
        keyboard = create_inline_kb(1, url=('Сылка на мероприятие', event_url), last_btn='Назад')
        await callback.message.answer(text='Мероприятие сегодня', reply_markup=keyboard)
    else:
        keyboard = create_inline_kb(1, url=('Сылка на мероприятие', event_url), last_btn='Назад')
        await callback.message.answer(text=f'Мероприятие запланировано на {event_date}', reply_markup=keyboard)
