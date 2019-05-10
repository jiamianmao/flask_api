"""
    作者：SpawN
    日期：2019/5/8 10:27
"""


class Scope:
    allow_api = set()
    allow_module = set()
    forbidden = set()

    def __add__(self, other):
        self.allow_api = self.allow_api | other.allow_api
        self.allow_module = self.allow_module | other.allow_module
        self.forbidden = self.forbidden | other.forbidden
        return self


class UserScope(Scope):
    allow_api = { 'v1.user+get_user', 'v1.user+delete_user' }


class SuperScope(Scope):
    allow_module = { 'v1.user' }


# 因为同一个 url 中会对应多个视图函数，而仅仅是HTTP 动词的不同，所以不应对 url 进行权限控制，而应该对视图函数控制
def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    # 在 Redprint 注册时增加 视图函数 所在的模块
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    return (endpoint in scope.allow_api) or (red_name in scope.allow_module)
