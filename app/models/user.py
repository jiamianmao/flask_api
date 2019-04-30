"""
    作者：SpawN
    日期：2019/4/29 16:52
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    account = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    # 代表权限，默认是 普通用户 1
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    @staticmethod
    def register_by_email(nickname, account, secret):
        print(nickname, account, secret)
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.account = account
            user.password = secret
            db.session.add(user)
