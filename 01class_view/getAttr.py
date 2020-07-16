# class MethodView:
#     def get(self):
#         print('get')
#         return 'get'
#
#     def post(self):
#         print('post')
#         return 'post'
#
#     def dispatch_request(self):
#         func = getattr(self, 'get', None)
#         return func()  # get()
#
#
# MethodView().dispatch_request()
from flask import Flask, request, render_template
from flask.views import View, MethodView

app = Flask(__name__)


# 斜杠形式
class UserView(MethodView):
    def get(self, project_id):
        if project_id is None:
            return 'Get all project'
        return f'get {project_id}'

    def post(self, project_id):
        return f'post'

    def put(self, project_id):
        return f'put {project_id}'

    def delete(self, project_id):
        return f'delete {project_id}'


f = UserView.as_view('user')
app.add_url_rule('/projects/<project_id>', view_func=f, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/projects/', defaults={"project_id": None}, view_func=f, methods=['GET', ])


# 问好形式
class UserViewDemo(MethodView):
    def get(self):
        project_id = request.args.get('p_id')
        if project_id is None:
            return 'Get all project'
        return f'get {project_id}'

    def post(self):
        return f'post'

    def put(self):
        project_id = request.args.get('p_id')
        return f'put {project_id}'

    def delete(self):
        project_id = request.args.get('p_id')
        return f'delete {project_id}'


f = UserView.as_view('user')
app.add_url_rule('/projects/', view_func=f, methods=['GET', 'POST', 'PUT', 'DELETE'])





