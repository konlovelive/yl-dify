import json

from accounts.forms import RegisterForm, LoginForm
from bson import Code
from conf import conn
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import logout_user, login_required
import pprint

from models import User
from utils.redis_utils import create_token

accounts = Blueprint('accounts', __name__,
                     template_folder='templates',
                     static_folder='../assets')


""" 登录页面 """
# 路由函数：登录页面（GET请求）
@accounts.route('/login', methods=['GET'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)

# 路由函数：登录（POST请求）
@accounts.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    # 获取请求中的 next 参数，如果不存在则使用 url_for('qa.index') 得到默认的跳转链接。
    next_url = request.values.get('next', url_for('qa.index'))
    if form.validate():  # 检查用户提交的表单数据是否通过了验证
        user = form.do_login()
        if user:
            # 4. 跳转到首页
            flash('{}, 欢迎回到csdn'.format(user.nickname), 'success')  # 传递给首页的flash消息
            return redirect(url_for('qa.index'))  # 重定向用户到之前获取的 next 参数指定的链接。
        else:
            flash('登录失败，请稍后重试', 'danger')
    return render_template('login.html', form=form, next_url=next_url)
#


@accounts.route('/login', methods=["POST"])
def login():
    '''
            用户登录
            :return:token
            '''
    data = request.get_data()  # 从请求中获取原始数据，发送的是 JSON 数据，那么 request.get_data() 也可以获取到这些数据。
    data = str(data, 'utf-8')  # 将原始数据从字节转换为字符串
    res_dir = json.loads(data)  # 将字符串转换为字典，以解析前端传递的 JSON 数据。
    print(res_dir)
    if res_dir is None:
        # return NO_PARAMETER()#检查是否成功解析 JSON 数据，如果没有解析成功，返回相应的错误。
        print(" res_dir is None")
        return None

    # 获取前端传过来的参数
    username = res_dir.get("username")
    password = res_dir.get("password")

    # 校验参数：确保用户名和密码都不为空
    if not all([username, password]):  # 检查 username 和 password 是否同时存在，如果有任何一个是空值或者为假（False），那么条件就会被满足。
        # code 是键，Code.NOT_NULL.value 是值。
        return jsonify(code=Code.NOT_NULL.value, msg="用户名和密码不能为空")  # jsonify:用于生成 JSON 响应的函数

    try:
        user = User.query.filter_by(user_name=username).first()  # SQLAlchemy
    except Exception as e:
        print("login error：{}".format(e))
        return jsonify(code=Code.REQUEST_ERROR.value, msg="获取信息失败")
    if user is None or not user.check_pwd(password) or user.del_flag == 2 or user.status == 2:
        return jsonify(code=Code.ERR_PWD.value, msg="用户名或密码错误")

        # 获取用户信息，传入生成token的方法，并接收返回的token
        # 获取用户角色
        #user_role = Role.query.join(UserRole, Role.id == UserRole.role_id).join(User,UserRole.user_id == user.id).filter(User.id == user.id).all()
    # role_list = [i.role_key for i in user_role]
    token = create_token(user.id, user.user_name, role_list)
    data = {'token': token, 'userId': user.id, 'userName': user.user_name, 'nickname': user.nickname}
    # 记录登录ip将token存入rerdis
    try:
        user.login_ip = request.remote_addr
        print(user)
        user.update()
        Redis.write(f"token_{user.user_name}", token)
    except Exception as e:
        print(e)
        return jsonify(code=Code.UPDATE_DB_ERROR.value, msg="登录失败:" + str(e))
    if token:
        # 把token返回给前端
        return jsonify(code=Code.SUCCESS.value, msg="登录成功", data=data)
    else:
        return jsonify(code=Code.REQUEST_ERROR.value, msg="请求失败", data=token)


    """ 注册 """
@accounts.route('/register', methods=['GET'])
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
@accounts.route('/register', methods=['POST'])
def register():
    form = RegisterForm()
    print("回到注册页面view")
    if form.validate_on_submit():
        user_obj = form.register()
        if user_obj:
            # 跳转到登录的页面
            flash('注册成功，请登录', 'success')
            return redirect(url_for('accounts.login'))
        else:
            flash('注册失败，请稍后再试', 'danger')
    # print(pprint.pprint(vars(form)))
    # 表单对象传递给模板文件，以便在模板中渲染和展示表单。
    return render_template('register.html', form=form)
#登录拦截器，意思是在客户端访问某些接口时，需要先进行登录验证，通过以后才能正常访问。


@user.route('/check_token',  methods=["POST"])
def check_token():
     # 在请求头上拿到token
     token = request.headers["Authorization"]
     user = verify_token(token)
     if user:
         key = f"token_{user.get('name')}"
         redis_token = Redis.read(key)
         if redis_token == token:
            return  SUCCESS(data=user.get('id'))
         else:
            return OTHER_LOGIN()
     else:
         return AUTH_ERR()


@accounts.route('/logout', methods=['GET'])
@login_required  # 使用装饰器限制访问
def logout():
    """ 退出登录 """
    # 自定义登录的逻辑代码
    # session['user_id'] = ''
    # g.current_user = None
    logout_user()
    conn.close()
    flash('当前账号已登出，欢迎下次再来', 'success')
    return redirect(url_for('accounts.login'))
