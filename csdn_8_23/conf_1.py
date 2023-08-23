import os


class Config(object):
    """ 项目的配置文件 """
    # 数据库连接URI
    # 数据库URI(连接地址)格式:协议名://用户名:密码@数据库IP:端口号/数据库名
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mima4748@localhost:3306/flask_qa'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # flash, form wtf
    SECRET_KEY = 'abcdsacb12312'
    # 文件上传的根路径
    MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'medias')


