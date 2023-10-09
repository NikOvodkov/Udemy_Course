from loader import dp
from .private_chat import IsPrivate
from .test_filter import SomeF
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    pass


if __name__ == 'filters':
    dp.filters_factory.bind(SomeF)


