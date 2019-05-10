"""
    作者：SpawN
    日期：2019/5/8 14:06
"""
from sqlalchemy import Column, Integer, String, orm
from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30))
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    # 在初始化模型时，并不会调用 __init__ 方法
    # https://docs.sqlalchemy.org/en/14/orm/constructors.html#sqlalchemy.orm.reconstructor
    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'binding', 'publisher', 'price', 'pages', 'pubdate', 'isbn', 'summary', 'image']
