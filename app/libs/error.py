"""
    作者：SpawN
    日期：2019/5/6 16:46
"""
from flask import request, json, Response
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg

        # r = {
        #     "haha": "xixi"
        # }
        # response = Response(json.dumps(r), mimetype='application/json')
        # super(APIException, self).__init__(msg, response)
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = {
            "msg": self.msg,
            "error_msg": self.error_code,
            "request": request.method + ' ' + self.get_url_no_param()
        }
        return json.dumps(body)

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json")]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
