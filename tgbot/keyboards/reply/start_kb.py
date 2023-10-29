from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.lexicon.lexicon_ru import lexicon_reply_kb

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

''''# Создаем кнопки с ответами согласия и отказа
donate = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)'''


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
        one_time_keyboard=True,
        resize_keyboard=True)


'''from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.lexicon.lexicon_ru import LEXICON_RU

# Функция для генерации инлайн-клавиатур
def create_event_kb(width: int,
                     *args: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()

    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args
    for button in args:
        buttons.append(InlineKeyboardButton(
                text=LEXICON_RU[button] if button in LEXICON_RU else button,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()'''
