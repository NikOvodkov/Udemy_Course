from aiogram import types

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), user_id=[497725007], text='secret')
@dp.message_handler(IsPrivate(), user_id=[497725007], text='admin')
async def admin_chat_secret(message: types.Message):
    await message.answer('Это секретное сообщение, вызванное одним из админов в личной переписке')