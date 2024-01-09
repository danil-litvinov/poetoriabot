from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from tgbot.misc.states import FSMTest



support_router = Router()

#message.forward_from_chat.id

@support_router.message(Command(commands='sup'))
async def sup_start(message: Message, state: FSMContext):
    await message.answer(text='Напишите ваше сообщение для специалиста поддержки.')
    await state.set_state(FSMTest.test_state)

@support_router.message(Command(commands='exit'), StateFilter(FSMTest.test_state))
async def sup_exit(message: Message, state: FSMContext):
    await message.answer(text='Вы вышли из режима службы поддержки')
    await state.clear()

@support_router.message(StateFilter(FSMTest.test_state))
async def sup_answer(message: Message, state: FSMContext, bot: Bot):
    await message.answer(text='Скоро ответим вам')
    await bot.send_message(chat_id=-1002100319628, text=f'Обращение: #ID{message.chat.id}\n\nТекст сообщения:\n{message.text}')
    #await bot.send_message(chat_id=1008810442, text=message.text)
    #await message.forward(chat_id=-1002100319628)
