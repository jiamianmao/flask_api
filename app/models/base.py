"""
    作者：SpawN
    日期：2019/4/30 17:23
"""
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy, BaseQuery
from sqlalchemy import Column, String, SmallInteger
from datetime import datetime
from contextlib import contextmanager

from app.libs.error_code import NotFound


class SQLAlchemy(BaseSQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs:
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, description=None):
        rv = self.get(ident)
        if rv is None:
            raise  NotFound()
        return rv

    def first_or_404(self, description=None):
        rv = self.first()
        if rv is None:
            raise NotFound()
        return rv

db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    __abstract__ = True

    create_time = Column(String(20))
    status = Column(SmallInteger, default=1)

    # 这里不能直接 create_time 的取值写在类变量中，在实例中才是最新的时间
    def __init__(self):
        self.create_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

    def set_attrs(self, obj):
        for key, value in obj.itmes():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item)

    def delete(self):
        self.status = 0

    # 一个模型返回的字段取决于 keys 这个列表
    def keys(self):
        return self.fields

    # 对 keys 进行过滤即可
    def hide(self, *args):
        # 我这里这样处理是因为我把 fields 设为类变量，第一次的操作会影响后续的操作，为了防止报错 这样处理
        # 但是我们在 /book/<isbn>/detail 中还需要这个 summary ，所以不能把 fields 设为类变量，但是在 SQLAlchemy 中
        # if field in self.fields:
        #     self.fields.remove(field)
        for item in args:
            self.fields.remove(item)
        return self
