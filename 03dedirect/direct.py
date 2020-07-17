from flask import Flask, request, redirect, url_for, render_template, abort, make_response, jsonify

app = Flask(__name__, static_url_path='/src')
# url和视图函数是绑定关系 ==> endpoint 断点


# 全局错误处理
@app.errorhandler(500)
def server_error(error):
    return render_template('error_500.html')


@app.errorhandler(404)
def server_error(error):
    return render_template('user_error_401.html')


# app.register_error_handler(500, server_error)


class UserError(Exception):
    pass


@app.errorhandler(UserError)
def server_error(error):
    # return render_template('user_error_401.html', error=error), 401
    res = jsonify({'msg': '401'})
    res.status = '401'
    return res


@app.route('/')
def index():
    # if request.args.get('username') is None:
    #     # return redirect('/login') 第一种方式
    #     return redirect(url_for('login', project_id='3', username='apple'))  # 第二种方式
    if not request.args.get('username'):
        # return render_template('user_error_404.html'), 401
        raise UserError('user error')
        # abort(404)
        # abort(make_response(render_template('user_error_404.html'), 404))
    return render_template('index.html')


@app.route('/login', endpoint='login')
def login():
    return 'login'


if __name__ == '__main__':
    app.run(debug=False)


'''
对于不可预知的错误：自定义500
@app.errorhandler(500)
def server_error(error):
    return render_template('error_500.html')
对于可以预知的错误：两种编程模式
函数里面如果有多个return，确保return的类型是一致的
1. return
@app.route('/)
def index():
    if not request.args.get('username'):
        return make_response('<p>401 没有授权</p>', 401)
    return 'index'
2. abort函数
@app.route('/)
def index():
    if not request.args.get('username'):
        abort(401)
    return 'index'
'''


