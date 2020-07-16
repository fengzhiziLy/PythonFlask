# pip install flask
# Werkzeug(application) Jinja2(渲染HTML)
import time

from flask import Flask, request, render_template, Config

# 初始化application
app = Flask(
    __name__,
    template_folder='html_file',  # 自己设置规则
    static_url_path='/src',  # 控制前端访问的时候告诉用户，哪一个URL地址下面保存了静态文件
    static_folder='src'
)

# 配置项
# python数据类型：字典  不可变字典  类：不同的属性setattr getattr
# Config
app.config['DEBUG'] = True
app.config['PORT'] = 5002


# 装饰器  可以统计流量
def log_time(f):
    def decorator(*args, **kwargs):
        print(f'{time.time()}')
        return f(*args, **kwargs)
        # 不要return其他的，否则会被作为response 包装
    return decorator


# 添加路由
# 如果不添加会报错404，因为没有定义根目录的处理逻辑
# 处理URL和函数之间的绑定关系的程序就叫路由
@app.route('/')
@app.route('/hello')
@log_time  # 必须放在里面 装饰器返回值必须是视图函数的返回值
def index():
    # 1.接收参数
    # 2.调用对应的函数去处理函数 model
    # 3.构建响应结果
    # 请求数据
    args = request.args
    name = args.get('username')
    print(name)
    # return '<p style="color:blue">hello</p>'
    return render_template('index.html')


# 运行服务器
# 两种启动方式
if __name__ == '__main__':  # __name__是标识模块的名字的一个系统变量
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])  # 重新启功，在前端显示错误信息
# 第二种方式命令行运行flask run  set FLASK_APP=app.py  set FLASK_ENV=development






