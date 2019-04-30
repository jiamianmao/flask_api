"""
    作者：SpawN
    日期：2019/4/29 16:22
"""
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 小程序 / 微信
    USER_MINI = 200
    USER_WX = 201
