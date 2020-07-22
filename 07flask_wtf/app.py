import os
import re

from flask import Flask, render_template, request

from helpers.forms import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello():
    return 'hello'


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

