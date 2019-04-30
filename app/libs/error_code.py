"""
    作者：SpawN
    日期：2019/4/30 9:44
"""
from app.libs.error import APIException

class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0

class ServerError(APIException):
    pass

class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1000
