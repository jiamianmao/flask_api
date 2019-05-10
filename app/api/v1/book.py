"""
    作者：SpawN
    日期：2019/4/30 16:25
"""
from flask import jsonify, request
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.models.book import Book
from app.validators.forms import BookSearchForm

api = Redprint('book')


@api.route('/search')
def search():
    # v1/book/search?q={}
    form = BookSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'
    books = Book.query.filter(or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)


@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)
