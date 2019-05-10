"""
    作者：SpawN
    日期：2019/4/30 16:25
"""
from datetime import date
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        return ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
