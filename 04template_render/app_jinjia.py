import json
import time
from datetime import datetime

from flask import Flask, make_response, jsonify, render_template, flash, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'APPLE'


# @app.template_filter('s_time')
def str_time(timestamp):
    return datetime.fromtimestamp(timestamp)


# 自定义测试
@app.template_test()
def jsoned(my_str):
    try:
        json.loads(my_str)
        return True
    except ValueError:
        return False


app.add_template_filter(str_time, 's_time')


# 环境处理器
@app.context_processor
def add_ctx():
    def str_x_time(timestamp):
        return datetime.fromtimestamp(timestamp)
    return {"user": ["apple", "疯子"], "c_time": str_x_time}


@app.route('/')
def index():
    projects = [
        {"name": "projectOne", "interface_num": 23, "create_time": int(time.time())},
        {"name": "projectTwo", "interface_num": 24, "create_time": int(time.time())},
        {"name": "projectThree", "interface_num": 25, "create_time": int(time.time())}
    ]
    flash('欢迎来到首页')
    flash('风之子')
    return render_template(
        'index.html', p=projects, title='风之子', msg='欢迎来到首页', msgOne=None,
        test_json='{"username": "apple"}'
    )


@app.route('/login/<username>')
def login(username):
    session['user'] = username
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


