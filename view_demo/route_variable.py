from flask import Flask

# from PythonFlask import urls  # 会造成循环导入

# print(uuid.uuid4())

app = Flask(__name__)

from view_demo.urls import *

# print(app.url_map)  # Map([<Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])
#
#
# @app.route('/')
# def home():
#     return 'home'

# 装饰器注册
# @app.route('/cases', methods=['GET'], endpoint='case', defaults={'id': 3})
# def get_case():
#     print(f'now is get cases {id}')
#     return 'cases'
#
#
# print(app.url_map)  # Map([<Rule '/cases' (OPTIONS, GET, HEAD) -> get_case>,
# <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])


if __name__ == '__main__':
    app.run(debug=True)




