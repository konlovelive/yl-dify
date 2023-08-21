# from flask import Flask, session, g
# from flask_login import LoginManager
# import mysql.connector
# from models import db, User
# from accounts.views import accounts
# from qa.views import qa
#
# from utils.filters import number_split
# from flask_oauthlib.client import OAuth
#
# app = Flask(__name__, static_folder='assets')#static_folder:指定了静态文件通常放在一个专门的文件夹中，供浏览器访问的存放路径
# #静态文件（例如 CSS、JavaScript、图像文件等），默认情况下，Flask 会在应用的根目录下寻找名为 static 的文件夹来存放静态文件。
# """单点登录"""
# # #  Flask 应用并配置 OAuth 2.0 客户端：
# # oauth = OAuth(app)
# #
# # # 配置 OAuth 2.0 客户端
# # oauth_app = oauth.remote_app(# oauth.remote_app() 函数创建了一个 OAuth 2.0 客户端实例，并传入了一些参数来配置客户端的行为。
# #     'example',# 指定客户端名称，你可以自行命名。它用于在会话中标识当前的 OAuth 2.0 客户端。
# #     consumer_key='your_client_id',
# #     consumer_secret='your_client_secret',
# #     request_token_params={'scope': 'email'},
# #     base_url='https://api.example.com/',
# #     request_token_url=None,
# #     access_token_method='POST',
# #     access_token_url='https://api.example.com/oauth/token',
# #     authorize_url='https://api.example.com/oauth/authorize'
# # )
#
# #from flask_cas import CAS
# #CAS(app) #  Flask 应用就可以使用 Flask-CAS 提供的功能，实现 CAS 单点登录认证。
#
#
#
# # 从配置文件加载配置
# app.config.from_object('conf.Config')
#
# # 数据库初始化
# db.init_app(app)
#
# # 登录验证
# login_manager = LoginManager()
# login_manager.login_view = "accounts.login"
# login_manager.login_message = '请登录'
# login_manager.login_message_category = "danger"
# login_manager.init_app(app)
#
# # 注册蓝图
# app.register_blueprint(accounts, url_prefix='/accounts')
# app.register_blueprint(qa, url_prefix='/')
#
# # 注册过滤器
# app.jinja_env.filters['number_split'] = number_split
#
# #
# # @app.before_request
# # def before_request():
# #     """ 如果有用户id,设置到全局对象 """
# #     user_id = session.get('user_id', None)
# #     if user_id:
# #         user = User.query.get(user_id)
# #         print(user)
# #         g.current_user = user
#
#
#
#
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)#使用 SQLAlchemy 的查询语法，查询数据库中具有指定 user_id 的用户对象
