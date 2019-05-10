"""
    作者：SpawN
    日期：2019/5/7 15:33
"""
from flask import jsonify, g
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.user import User
from app.libs.token_auth import auth

api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    print(2)
    uid = g.user.uid
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return Success(msg='删除成功')


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return Success(msg='删除成功')
