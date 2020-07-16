import time

from flask import Flask, request, render_template
from flask.views import View, MethodView

app = Flask(__name__)


class ProjectView(MethodView):
    def get(self):
        return 'get'

    def post(self):
        return 'post'


f = ProjectView.as_view('project')
app.add_url_rule('/project', view_func=f)

if __name__ == '__main__':
    app.run()





