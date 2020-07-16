# 搭建服务
# 监听动作 while
# 处理程序
# 返回数据到套接字，生成一个响应对象
import json
from wsgiref.simple_server import make_server


def home(request):
    return request


def login(request):
    return request


def projects(request):
    return request


patterns = {
    '/': home,
    '/login': login,
    '/projects': projects
}


def app(env, start_response):
    """
    如果出现了很多的条件分支都是 == ，使用字典去封装
    :param env:
    :param start_response:
    :return:
    """
    # env 获取请求相关数据
    # start_response 状态码 head 元组不可以修改
    url = env.get('PATH_INFO')
    params = env.get('QUERY_STRING')
    if url is None or url not in patterns.keys():
        # start_response('404 not found', [('content-type', 'text/html')])
        start_response('404 not found', [('content-type', 'application/json')])
        msg = json.dumps({"msg": "page not found"})
        return [msg.encode()]
        # return [b'<p style="color:red">page not found</p>']  # b type
    start_response('200 OK', [('content-type', 'text/plain')])
    resp = patterns.get(url)
    if resp is None:
        start_response('404 not found', [('content-type', 'text/html')])
        return [b'<p style="color:red">page not found</p>']  # b type
    return [resp(params).encode()]

    # if env.get('PATH_INFO') == '/':
    #     start_response('200 OK', [('content-type', 'text/plain')])
    #     resp = home()
    #     return [resp.encode()]
    # elif env.get('PATH_INFO') == '/login':
    #     start_response('200 OK', [('content-type', 'text/plain')])
    #     resp = login()
    #     return [resp.encode()]
    # elif env.get('PATH_INFO') == '/projects':
    #     start_response('200 OK', [('content-type', 'text/plain')])
    #     resp = projects()
    #     return [resp.encode()]
    # else:
    #     start_response('404 not found', [('content-type', 'text/plain')])
    #     return [b'{page not found}']  # b type


# flask/django ==> application
# flask run  django run ==> WSGI协议
# uwsgi / gunicorn / tornado / nginx
server = make_server("", 6001, app)  # app 回调
server.serve_forever()

