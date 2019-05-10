"""
    作者：SpawN
    日期：2019/4/30 16:46
"""
from flask import Blueprint
from . import book, client, token, user, gift

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    user.api.register(bp_v1)
    gift.api.register(bp_v1)
    return bp_v1
