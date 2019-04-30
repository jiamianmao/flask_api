"""
    作者：SpawN
    日期：2019/4/29 16:58
"""
from contextlib import contextmanager
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy, BaseQuery
from sqlalchemy import Column, String, SmallInteger

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
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    __abstract__ = True

    create_time = Column(String(20))
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

    def set_attrs(self, obj):
        for key, value in obj.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
