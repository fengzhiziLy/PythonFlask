import json

from flask import Flask, make_response, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    # 构造一个响应头 第一种方式
    # return json.dumps({"username": "python"}), 201, {"content-type": "application/json"}
    # make_response() 第二种方式 Response()
    # r = make_response(json.dumps({"username": "pythonDemo"}), {"content-type": "text/html"})
    # r.status = '203'
    # r.content_type = 'application/json'
    r = jsonify({"username": "风之子"})  # flask自己封装的方法
    # 修改状态码
    r.status = '201'
    return r


if __name__ == '__main__':
    app.run(debug=True)





