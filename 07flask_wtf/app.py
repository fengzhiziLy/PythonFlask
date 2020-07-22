import os
import re

import pymysql as pymysql
from flask import Flask, render_template, request, abort, g, session

from helpers.forms import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


# 场景：数据埋点，也就是类似某一个请求的数量之类的
@app.before_request
def get_num_of_interface():
    # sign = request.args.get('sign')
    # # 验证sign是否通过
    # if sign != 'admin':
    #     abort(401)
    # # 访问数据库，统计信息
    # print('接口访问数量的缓存+1')
    # a = sign + 'md'
    pass
    # g.user = a


@app.after_request
def make_res(response):
    response.headers['server'] = 'icon'
    return response


@app.teardown_request
def tear_make_res(error):
    print(error)
    print("tear down")


@app.before_first_request
def set_server_name():
    print('setting server name')


def connect_to_database():
    conn = pymysql.connect(host='localhost', user='root', password='111111', db='employees', charset='utf8mb4')
    return conn.cursor()


@app.before_request
def get_db():
    if 'db' not in g:
        g.db = connect_to_database()


@app.teardown_request
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def hello():
    # print(g.user)
    # g.db.execute('SELECT * FROM departments;')
    # a = g.db.fetchall()
    # print('数据', a)
    if not session.get('user'):
        abort(401)
    print(session.get('user'))
    return 'hello'


@app.route('/login')
def login():
    username = request.args.get('username')
    pwd = request.args.get('pwd')
    if username and pwd:
        session['user'] = username
        return '登录成功'
    return '没有登录'


@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
    return '退出登录'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(formdata=request.form)
    if request.method == 'GET':
        return render_template('register.html', form=form)
    # post 验证表单
    # form = RegisterForm(request.form)
    if form.validate():  # 验证主函数
        print(form.data)  # 获取所有的信息
        return 'success'
    return f'error: {form.errors}'


if __name__ == '__main__':
    app.run(debug=True)


'''
全局变量
@app.before_request 统计流量、签名、请求时间验证
集中注册：@after_request  场景：封装响应信息，修改响应信息   如果视图出现错误，就不会调用
@app.teardown_request 通常用来释放资源，不管有没有报错都会调用
@app.before_first_request
g 同一个请求共享数据 验证用户信息,连接数据库
'''

