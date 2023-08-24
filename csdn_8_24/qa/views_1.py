from flask import Blueprint, render_template, request, abort
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import User, db
from flask_sqlalchemy import SQLAlchemy

from utils import constants


qa = Blueprint('qa', __name__,
               template_folder='templates',
               static_folder='../assets')

# 创建数据库实例
# db = SQLAlchemy()  在models.py中已经创建了，只能创建一个

# 创建模型类--爬取到的首页数据
class index_spider_data(db.Model):
    __tablename__ = 'csdn_index_links'  # 将db选择为指定的表名
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(500))
    title= db.Column(db.String(500))
    desc = db.Column(db.Text)
    agree = db.Column(db.Text)
    disagree = db.Column(db.Text)
    author = db.Column(db.Text)


@qa.route('/')
@login_required
def index():
    """ 首页 """
    print("受保护的首页")

    # 从数据库中获取所有文章
    posts = index_spider_data.query.all()
    return render_template('index.html', posts=posts)


