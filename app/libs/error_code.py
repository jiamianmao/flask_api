"""
    作者：SpawN
    日期：2019/5/6 16:53
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


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    msg = 'forbidden'
    error_code = 1006


class DuplicateGift(APIException):
    code = 400
    msg = '重复添加'
    error_code = 1007