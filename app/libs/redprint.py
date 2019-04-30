"""
    作者：SpawN
    日期：2019/4/29 14:52
"""

class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            # endpoint = options.pop('endpoint', None)
            # self.add_url_rule(rule, endpoint, f, **options)
            # 这里因为没有 Blueprint 对象，所以先保存起来
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            # 相当于去掉字典中指定的一项
            endpoint = options.pop('endpoint', None)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
