from flask import Flask, make_response, jsonify, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'APPLE'


@app.route('/')
def index():
    projects = [
        {"name": "项目1", "interface_num": 23, "create_time": "2020/07/16"},
        {"name": "项目2", "interface_num": 24, "create_time": "2020/07/16"},
        {"name": "项目3", "interface_num": 25, "create_time": "2020/07/16"}
    ]
    flash('欢迎来到首页')
    flash('风之子')
    return render_template('index.html', p=projects, title='风之子', msg='欢迎来到首页')


if __name__ == '__main__':
    app.run(debug=True)


