from accounts.forms import RegisterForm, LoginForm
from conf import conn
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import logout_user, login_required
import pprint

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
