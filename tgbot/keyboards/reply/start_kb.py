from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.lexicon.lexicon_ru import lexicon_reply_kb


def create_reply_kb(width: int,
                    *args: str) -> ReplyKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = ReplyKeyboardBuilder()

    # Инициализируем список для кнопок
    buttons: list[KeyboardButton] = []

    # Заполняем список кнопками из аргументов args
    for button in args:
        buttons.append(KeyboardButton(
                text=lexicon_reply_kb[button] if button in lexicon_reply_kb else button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup(
        #one_time_keyboard=True,
        resize_keyboard=True)
