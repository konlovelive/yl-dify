# from datetime import datetime
#
#  from flask_sqlalchemy import SQLAlchemy
#
# from utils import constants
#
# # 创建数据库实例
# db = SQLAlchemy()
#
#
# class User(db.Model):
#     """ 用户模型 """
#     __tablename__ = 'accounts_user'# autoincrement=True：表示主键值自动递增
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
#     # 用户名，用于登录
#     username = db.Column(db.String(64), unique=True, nullable=False)
#     # 用户昵称
#     nickname = db.Column(db.String(64))
#     password = db.Column(db.String(256), nullable=False)
#     # 用户的头像地址
#     avatar = db.Column(db.String(256))
#
#     # 是否有效，无效用户将不能登录系统
#     status = db.Column(db.SmallInteger,
#                        default=constants.UserStatus.USER_ACTIVE.value,
#                        comment='用户状态')
#     # 是否是超级管理员，管理员可以对所有内容进行管理
#     is_super = db.Column(db.SmallInteger,
#                          default=constants.UserRole.COMMON.value)
#     # 创建时间
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     # 最后修改的时间
#     updated_at = db.Column(db.DateTime,
#                            default=datetime.now, onupdate=datetime.now)
#     # profile = db.relationship('UserProfile')
#
        #这些函数需要在User类的实例中显示调用，不会在创建实例时自动调用
#     @property # @property 是 Python 中的一个装饰器，用于将一个方法转换为属性访问，使方法可以像属性一样被访问，不需要加括号调用。
#     def is_authenticated(self):
#         return True
#
#     @property
#     def is_active(self):
#         """ 有效的用户才能登录系统 """
#         return self.status == constants.UserStatus.USER_ACTIVE.value
#
#     @property
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return '{}'.format(self.id)
#
#     def __str__(self):
#         return self.nickname