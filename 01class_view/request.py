from flask import Flask, request, render_template
from flask.views import View, MethodView

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    a = request
    # get请求 request请求相关  flask中APP wsgi:环境变量
    get_data = request.args
    # post表单数据
    form_data = request.form
    # json
    json_data = request.json
    file_data = request.files
    # ajax json,请求头XHR信息
    return 'index'


app.run(debug=True)

"""
路由设计：
project projects
前后端不分离，模板渲染： 一个视图函数写一个URL
url: 获取所有的项目：/projects def list_projects()
url: 获取单个项目内容：/project/<id> def get_project()
url: 修改某个项目内容：/project_edit/<id> def edit_project()

前后端分离： rest method:get, put, post, delete
/project/<id> 类的视图：def get:单个资源
/projects
"""


