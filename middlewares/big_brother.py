import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info('[----------------Новый апдейт!-----------------------]')
        logging.info('1. Pre Process Update')
        logging.info('Следующая точка: Process Update')
        data['middleware_data'] = 'Это пройдёт до on_post_process_update'
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        if user in banned_users:
            raise CancelHandler()

    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f'2. Process Update, {data=}')
        logging.info('Следующая точка: Pre Process Message')

    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info(f'3. Pre Process Message, {data=}')
        logging.info('Следующая точка: Filters, Process Message')
        data['middleware_data'] = 'Это пройдёт в on_process_message'

    async def on_process_message(self, message: types.Message, data: dict):
        logging.info('5. Process Message')
        logging.info('Следующая точка: Handler')
        data['middleware_data'] = 'Это попадёт в хендлер'

    async def on_post_process_message(self, message: types.Message, data_from_handler: list, data: dict):
        logging.info(f'7. Post Process Message, {data=}, {data_from_handler=}')
        logging.info('Следующая точка: Post Process Update')

    async def on_post_process_update(self, update: types.Update, data_from_handler: list, data: dict):
        logging.info(f'8. Post Process Update, {data=}, {data_from_handler=}')
        logging.info(f'[-------------------Выход----------------------]\n')


    async def on_pre_process_callback_query(self, cq: types.CallbackQuery, data: dict):
        await cq.answer()





