"""
    作者：SpawN
    日期：2019/4/30 16:28
"""
class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            # 这里没有 BP 对象，所以没有 add_url_rule 方法 这里可以先保存起来，因为在register中会有BP对象
            endpoint = options.pop("endpoint", f.__name__)
            # self.add_url_rule(rule, endpoint, f, **options)
            self.mound.append((rule, endpoint, f, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        # 这里是给 RP 注册到 BP 中，所以不是继承 BP 的register 方法
        if url_prefix is None:
            url_prefix = '/' + self.name
        for rule, endpoint, f, options in self.mound:
            # 这里的 endpoint 可以自定义，所以我们为了对权限控制增加模块级别的控制，需要对 endpoint 增加模块标识
            bp.add_url_rule(url_prefix + rule, self.name + '+' + endpoint, f, **options)
