from app.models.book import db
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 导入模块路径,使用此方法需要保证该模块中变量名全部大写，不然会被忽略掉
    app.config.from_object('app.setting')

    # 关联app和蓝图
    register_blueprint(app)

    # 关联app和数据模型
    db.init_app(app)
    db.create_all(app=app) # 创建数据表
    return app

def register_blueprint(app):
    from app.web.book import web  #函数内部导入
    app.register_blueprint(web)