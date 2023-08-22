from conf import conn
from flask import Flask, session, g
from flask_login import LoginManager
from flask_login import UserMixin# 导入UserMixin
import mysql.connector

from accounts.views import accounts
from qa.views import qa
from utils import constants

from utils.filters import number_split
from flask_oauthlib.client import OAuth

app = Flask(__name__, static_folder='assets')#static_folder:指定了静态文件通常放在一个专门的文件夹中，供浏览器访问的存放路径
#静态文件（例如 CSS、JavaScript、图像文件等），默认情况下，Flask 会在应用的根目录下寻找名为 static 的文件夹来存放静态文件。
"""单点登录"""
# #  Flask 应用并配置 OAuth 2.0 客户端：
# oauth = OAuth(app)
#
# # 配置 OAuth 2.0 客户端
# oauth_app = oauth.remote_app(# oauth.remote_app() 函数创建了一个 OAuth 2.0 客户端实例，并传入了一些参数来配置客户端的行为。
#     'example',# 指定客户端名称，你可以自行命名。它用于在会话中标识当前的 OAuth 2.0 客户端。
#     consumer_key='your_client_id',
#     consumer_secret='your_client_secret',
#     request_token_params={'scope': 'email'},
#     base_url='https://api.example.com/',
#     request_token_url=None,
#     access_token_method='POST',
#     access_token_url='https://api.example.com/oauth/token',
#     authorize_url='https://api.example.com/oauth/authorize'
# )

#from flask_cas import CAS
#CAS(app) #  Flask 应用就可以使用 Flask-CAS 提供的功能，实现 CAS 单点登录认证。



# 从配置文件加载配置
app.config.from_object('conf.Config')

# 数据库初始化
# db.init_app(app)

# Flask-Login 库的一部分，用于在 Flask 应用程序中管理用户身份验证和会话。
# 登录验证
login_manager = LoginManager()#创建一个 LoginManager 对象。
login_manager.login_view = "accounts.login"# 设置登录视图的名称。当未经身份验证的用户尝试访问需要登录的页面时，他们将被重定向到此视图
login_manager.login_message = '请登录'
login_manager.login_message_category = "danger"# 设置消息类别，用于在呈现消息时应用样式
login_manager.init_app(app)# 初始化 Flask 应用程序以使用 Flask-Login。

# 注册蓝图
app.register_blueprint(accounts, url_prefix='/accounts')# 该蓝图中定义的所有路由都将以 /accounts 作为前缀。
app.register_blueprint(qa, url_prefix='/')

# 注册过滤器
app.jinja_env.filters['number_split'] = number_split# 在 Jinja2 环境中注册一个名为 number_split 的过滤器

#
# @app.before_request
# def before_request():
#     """ 如果有用户id,设置到全局对象 """
#     user_id = session.get('user_id', None)
#     if user_id:
#         user = User.query.get(user_id)
#         print(user)
#         g.current_user = user





# user_loader 函数会在用户访问需要登录的页面时自动被调用，用于加载用户信息到会话中
@login_manager.user_loader
def load_user(user_id):
    # 基于 user_id 从数据库中加载用户信息
    # 通过自定义的函数或直接执行 MySQL 查询语句实现
    # 返回一个 User 对象

    # 创建游标
    cursor = conn.cursor()
    query ="SELECT * FROM accounts_user WHERE id = username"
    cursor.execute(query)

    # 获取查询结果
    result = cursor.fetchall()

    # 关闭游标和连接
    cursor.close()
    return result




