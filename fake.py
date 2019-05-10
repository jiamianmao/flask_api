"""
    作者：SpawN
    日期：2019/5/7 17:14
"""
from app.models.base import db
from app.models.user import User
from app import create_app

app = create_app()

with app.app_context():
    with db.auto_commit():
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.account = '999@qq.com'
        user.auth = 2
        db.session.add(user)
