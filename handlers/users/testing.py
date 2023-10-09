from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command('test'), state=None)
async def enter_test(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(str(data))
    await message.answer('Вы начали тестирование. \n'
                         'Вопрос №1. \n\n'
                         'Вы часто занимаетесь бессмысленными делами '
                         '(бесцельно блуждаете по интернету, клацаете пультом телевизора...')
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer('Вопрос №2. \n\n'
                         'Ваша память ухудшилась и вы помните то, что было давно, но забываете недавние события')
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text
    await message.answer('Спасибо за ваши ответы')
    await message.answer(f'Ответ 1: {answer1}')
    await message.answer(f'Ответ 2: {answer2}')
    await state.reset_state(with_data=False)
