"""
    作者：SpawN
    日期：2019/5/6 15:23
"""
from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.json
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        success = super(BaseForm, self).validate()
        if not success:
            raise ParameterException(msg=self.errors)
        return self