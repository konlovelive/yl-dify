import hashlib

# flask_login 用于处理用户认证和会话管理的Flask扩展，它提供了一些方便的功能，如登录、登出、记住用户。
from conf import conn
from flask_login import login_user
from flask_wtf import FlaskForm  # flask_wtf：快速定义表单模板、验证表单数据、实现全局的CSRF保护等
# wtforms：表单验证和渲染库
from models import User
from wtforms import StringField, PasswordField, ValidationError  # 三个类分别处理：文本输入（框）、密码输入（框）、异常类（掏出表单验证过程中的验证错误）
# 三个验证器类：分别用于检查字段的数据是否为“真值”、验证字符串的长度、用于比较两个字段
from wtforms.validators import DataRequired, Length, EqualTo

# 本地导入
from utils import constants
from utils.validators import phone_required


class RegisterForm(FlaskForm):
    """ 用户注册 """
    # 表单类中的一个字段定义，label：字段的标签，显示在页面上，render_kw：字段的渲染参数，可以设置 HTML 属性。
    username = StringField(label='用户名', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入用户名'  # placeholder：输入框的占位文本
        # validators：验证器列表，DataRequired 是 Flask-WTF 提供的一个验证器，它用于确保字段不为空。
    }, validators=[DataRequired('请输入用户名'), phone_required])  # phone_required自定义的验证函数，

    nickname = StringField(label='用户昵称', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入用户昵称'
    }, validators=[DataRequired('请输入用户昵称'),
                   Length(min=2, max=20, message='昵称长度在2-20之间')])

    password = PasswordField(label='密码', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入密码'
    }, validators=[DataRequired('请输入密码')])

    confirm_password = PasswordField(label='确认密码', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入确认密码'
    }, validators=[DataRequired('请输入确认密码'),
                   EqualTo('password', message='两次密码输入不一致')])
    # 定义 SQL 查询语句
    # select_user_query = '''
    #             SELECT * FROM accounts_user
    #             WHERE username = %s
    #             LIMIT 1  --LIMIT 1 表示查询只返回满足条件的第一条记录，即使有多条记录满足条件
    #             '''

    def validate_username(self, field):
        """ 检测用户名是否已经存在 """
        # User：自定义数据库模型类，filter_by()：查询过滤方法（位于SQLAlchemy中），过滤出用户名与传入的 field.data 相同的记录
        # 查询数据库中
        #user = User.query.filter_by(username=field.data).first()

       # user对象从模型
        user=User(self.username).get_name_record
        if user:
            raise ValidationError('该用户名已经存在')
        return field

    def register(self):
        """ 自定义的用户注册函数 """
        # 1. 获取表单信息
        username = self.username.data
        password = self.password.data
        nickname = self.nickname.data
        # 2. 添加到db.session
        try:
            # 将密码加密存储
            # password = hashlib.sha256(password.encode()).hexdigest()
            # user_obj = User(username=username, password=password, nickname=nickname)
            cursor = conn.cursor()  # 数据库游标
            sql = "INSERT INTO csdn_index_links(username,password,nickname) VALUES (%s,%s,%s);"
            cursor.execute(sql, [username,password,nickname])
            conn.commit()  # 并提交事务
            user_obj = cursor.fetchone()
            cursor.close()

            return user_obj# 返回结果不为空即可
        except Exception as e:
            print(e)
        return None


class LoginForm(FlaskForm):
    """ 用户登录 """
    username = StringField(label='用户名', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入用户名'
    }, validators=[DataRequired('请输入用户名'), phone_required])

    password = PasswordField(label='密码', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入密码'
    }, validators=[DataRequired('请输入密码')])

    # # 定义 SQL 查询语句
    # select_user_query = '''
    #             SELECT * FROM accounts_user
    #             WHERE username = %s AND password = %s
    #             LIMIT 1  -- LIMIT 1 表示查询只返回满足条件的第一条记录，即使有多条记录满足条件
    #             '''



    def print_name(self):
        print('用户登录-用户名' + self.username.data)
        print('用户登录-用户密码' + self.password.data)

    def validate(self):
        result = super().validate()
        username = self.username.data
        password = self.password.data
        if result:
            #  TODO 验证加密后的密码是否正确
            # cursor = conn.cursor()  # 数据库游标
            # sql = "INSERT INTO csdn_index_links(link,title,`desc`,agree,disagree,author) VALUES (%s,%s,%s,%s,%s,%s);"
            # user = User.query.filter_by(username=username, password=password).first()

            user_obj = User(username)
            user = user_obj.get_name_record()# get_name_record返回结果为空
            # 现在 user 变量中保存了满足条件的第一个记录，如果没有找到则 user 为 None
            # print(user)

            if user is None:
                result = False
                self.username.errors = ['用户名或者是密码错误']
            elif user[5] == constants.UserStatus.USER_IN_ACTIVE.value:
                result = False
                self.username.errors = ['用户已被禁用']
        return result

    def do_login(self):
        """ 执行登录逻辑代码 """
        username = self.username.data
        password = self.password.data
        try:
            # 1. 查找对应的用户
            # TODO 验证加密后的密码是否正确
            #user = User.query.filter_by(username=username, password=password).first()

            user_obj = User(username, password)
            user = user_obj.get_name_pwd_record()  # get_name_record返回结果为空

            # 2. 登录用户
            login_user(user_obj)

            print(user_obj)

            return user_obj
        except Exception as e:
            print(e)
        return None

