"""
    作者：SpawN
    日期：2019/4/29 13:42
"""
from app.libs.redprint import Redprint

api = Redprint('user')

@api.route('/')
def index():
    return 'index page!'
