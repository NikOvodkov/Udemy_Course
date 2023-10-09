import logging
import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate, SomeF
from loader import dp
from utils.db_api.models import User
from utils.misc import rate_limit


@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")))
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке,\n'
                         f'в вашей команде есть диплинк. \n'
                         f'Вы передали аргумент {deep_link_args}')


@rate_limit(5, key='start')
@dp.message_handler(CommandStart(), SomeF())
async def bot_start(message: types.Message, middleware_data, from_filter, user: User):
    deep_link = await get_start_link(payload='123')
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке,\n'
                         f'в вашей команде нет диплинка. {middleware_data=} {from_filter=}\n'
                         f'Ваша диплинк ссылка {deep_link}',
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                             [InlineKeyboardButton(text='Простая кнопка', callback_data='button')]]))
    logging.info('6. Handler')
    logging.info(f'Следующая точка: Post Process Message')
    return {'from_handler': 'Данные из хэндлера'}


@dp.callback_query_handler(text='button')
async def get_button(call: types.CallbackQuery):
    await call.message.answer('Вы нажали на кнопку')
