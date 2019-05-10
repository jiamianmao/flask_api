"""
    作者：SpawN
    日期：2019/4/30 17:17
"""
from sqlalchemy import Column, String, SmallInteger, Integer

from app.libs.error_code import NotFound, AuthFailed
from .base import Base, db
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    def keys(self):
        return ['id', 'account', 'nickname', 'auth']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.account = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(account=email).first_or_404()
        if not check_password_hash(user.password, password):
            raise AuthFailed()
        scope = 'SuperScope' if user.auth == 2 else 'UserScope'
        return {
            'uid': user.id,
            'scope': scope
        }
