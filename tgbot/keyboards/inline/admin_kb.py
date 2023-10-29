from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.lexicon.lexicon_ru import LEXICON_RU

def add_admin_button(keyboard: InlineKeyboardMarkup,
                     width: int,
                     *args: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb = keyboard

    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args
    for button in args:
        buttons.append(InlineKeyboardButton(
                text=LEXICON_RU[button] if button in LEXICON_RU else button,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb().add(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb