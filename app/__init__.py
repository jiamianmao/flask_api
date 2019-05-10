"""
    作者：SpawN
    日期：2019/5/7 15:31
"""
from .index import Flask


def register_config(app):
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)

def create_app():
    app = Flask(__name__)
    # 注册配置文件
    register_config(app)
    # 注册蓝图
    register_blueprint(app)
    # 注册插件
    register_plugin(app)
    return app