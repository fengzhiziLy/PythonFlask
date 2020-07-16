import time

from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__)


def log_time(f):
    def decorator(*args, **kwargs):
        print(f'{time.time()}')
        return f(*args, **kwargs)
        # 不要return其他的，否则会被作为response 包装
    return decorator


class ProjectView(View):
    # methods = ['GET', 'POST']
    # decorators = (log_time,)

    def get(self):
        return 'get'

    def post(self):
        return 'post'

    # 分配请求
    def dispatch_request(self):
        dispatch_pattern = {'GET': self.get, 'POST': self.post}
        method = request.method
        return dispatch_pattern.get(method)()
        # return 'project'


f = ProjectView.as_view('project')
log_time(f)

app.add_url_rule('/project', view_func=f, methods=['GET', "POST"])


if __name__ == '__main__':
    app.run(debug=True)
