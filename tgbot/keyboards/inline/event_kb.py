from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.lexicon.lexicon_ru import EVENTS


LEXICON = {
    'back_events': 'Назад',
    'next_btn': '->',
    'prev_btn': '<-',
}


# Функция для генерации инлайн-клавиатур
def create_inline_kb(width: int,
                     *args: str,
                    url: list[str],
                    last_btn: str | None = None,
                     **kwargs: str,) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    if url:
        kb_builder.row(InlineKeyboardButton(
            text=url[0],
            url=url[1]
        ))

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data='last_btn'
        ))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Функция для генерации клавиатуры с мероприятиями
def create_events_kb(width: int, 
                    *args: str,
                    back_button: bool = False) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for key in args:
        if key in EVENTS:
            buttons.append(InlineKeyboardButton(
                text=f"{EVENTS[key]['event_date']} {EVENTS[key]['event_name']}",
                callback_data=key
            ))

    if back_button:
        buttons.append(InlineKeyboardButton(
            text='Назад',
            callback_data='back'
        ))

    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()