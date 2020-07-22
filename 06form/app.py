import re

from flask import Flask, make_response, jsonify, render_template, flash, session, redirect, url_for, request, abort, \
    Response

app = Flask(__name__)


# def validate_register_form(form):


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    phone = request.form.get('phone')
    pwd = request.form.get('pwd')
    confirm_pwd = request.form.get('confirm_pwd')
    res = Response(render_template('register.html', msg='手机号码不能为空'), status='412', content_type='text/html;charset=utf-8')
    if not phone:
        # 提示：手机号码不能为空
        # abort(412, description='手机号码不能为空')
        abort(res)
    if not re.match(r'^1[3,5,7,8,9]\d{9}$', phone):
        abort(412, description='phone is error')
    if not pwd:
        abort(412, description='password is empty')
    if len(pwd) < 6:
        abort(412, description='password is not safe')
    if pwd != confirm_pwd:
        abort(412, description='password is not consistent')
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)

# 模板：继承、include、macro
