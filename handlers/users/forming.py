from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Form


@dp.message_handler(Command('form'), state=None)
async def enter_form(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # await message.answer(str(data))
    await message.answer('Введите своё имя')
    await Form.Q1.set()


@dp.message_handler(state=Form.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer('Введите свой email')
    await Form.next()


@dp.message_handler(state=Form.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer('Введите свой телефон')
    await Form.next()


@dp.message_handler(state=Form.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')
    answer3 = message.text
    await message.answer('Привет! Ты ввёл следующие данные:')
    await message.answer(f'Имя - "{answer1}"')
    await message.answer(f'Email - "{answer2}"')
    await message.answer(f'Телефон - "{answer3}"')
    await state.reset_state(with_data=True)
