"""
    作者：SpawN
    日期：2019/4/30 13:23
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        success = super(BaseForm, self).validate()
        if not success:
            raise ParameterException(msg=self.errors)
        return self
