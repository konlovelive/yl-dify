
# 注册蓝图
# 蓝图的名字，指定蓝图所在的包或者模块，路径
from flask import Blueprint

web=Blueprint('web',__name__)# 关联视图函数和蓝图

# 看似和web包里其他文件循环导入了，但是并没有
from app.web import book
from app.web import user