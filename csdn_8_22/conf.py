import os


import app
import mysql.connector

conn = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password='mima4748',
        database='flask_qa'
    )

class Config(object):
    """ 项目的配置文件 """
    # 数据库连接URI
    # 数据库URI(连接地址)格式:协议名://用户名:密码@数据库IP:端口号/数据库名
    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['MYSQL_USER'] = 'root'
    # app.config['MYSQL_PASSWORD'] = 'mima4748'
    # app.config['MYSQL_DB'] = 'flask_qa'

    # SQLALCHEMY_DATABASE_URI = 'mysql://root:mima4748@localhost:3306/flask_qa'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # flash, form wtf



    SECRET_KEY = 'abcdsacb12312'
    # 文件上传的根路径
    MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'medias')

    # 连接MySQL数据库

