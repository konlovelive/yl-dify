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

import redis
r=redis.Redis(
    host="localhost",
    port=6379,
    password="mima4748",
    db=0# 使用0号逻辑库
)

# redis连接池
pool=redis.ConnectionPool(
    host="localhost",
    port=6379,
    password="mima4748",
    db=0,
    max_connections=20# 最大连接数
)

# 从连接池里获取连接
r=redis.Redis(
    connection_pool=pool
)
r.set("country","英国")
r.set("city","伦敦")
city=r.get("city").decode("utf-8")# 需要转码
print(city)


# 删除连接对象的引用就行，连接对象本身会自动回收
del r
