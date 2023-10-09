from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from .big_brother import BigBrother
from .sentinel import Sentinel
from .acl import ACLMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ACLMiddleware())
    dp.middleware.setup(Sentinel())
    dp.middleware.setup(BigBrother())

