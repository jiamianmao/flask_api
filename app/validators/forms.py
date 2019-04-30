"""
    作者：SpawN
    日期：2019/4/29 16:34
"""
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError
from .base import BaseForm as Form

from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='邮箱输入不合法')])
    secret = StringField(validators=[DataRequired(), Regexp('^[A-Za-z0-9_*$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22, message='昵称不对哦')])

    def validate_account(self, value):
        if User.query.filter_by(account=value.data).first():
            raise ValidationError()

    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError('该昵称已被注册')
